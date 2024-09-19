from flask import Flask, render_template, request, redirect, url_for, flash, session
import sqlite3
import os
import csv
from werkzeug.security import generate_password_hash, check_password_hash
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes, padding
from base64 import b64encode, b64decode
import shutil

app = Flask(__name__)
app.secret_key = 'chave_secreta_para_flash'  # Necessário para usar o flash


# Função para criar o banco de dados e a tabela
def criar_bd():
    conn = sqlite3.connect('banco.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            senha TEXT NOT NULL,
            data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    conn.commit()
    conn.close()


# Função para gerar chave AES a partir de uma senha
def generate_key(password: str, salt: bytes):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,  # 32 bytes = 256 bits para AES-256
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    return kdf.derive(password.encode())  # Retorna a chave sem codificação base64


# Função para criptografar os dados
def encrypt_data(data, key):
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(data) + padder.finalize()

    iv = os.urandom(16)  # Vetor de inicialização
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()

    return iv + encrypted_data  # O IV é adicionado no início dos dados criptografados


# Função para descriptografar os dados
def decrypt_data(encrypted_data, key):
    iv = encrypted_data[:16]  # Extrai o IV
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_padded_data = decryptor.update(encrypted_data[16:]) + decryptor.finalize()

    unpadder = padding.PKCS7(128).unpadder()
    data = unpadder.update(decrypted_padded_data) + unpadder.finalize()

    return data


# Rota para visualizar o CSV criptografado (com POST)
@app.route('/visualizar_csv_post', methods=['POST'])
def visualizar_csv_post():
    csv_path = "transferencias_ficticias.csv"
    backup_folder = "backup"

    # Obtém a senha fornecida pelo usuário
    password = request.form['password']
    salt = b'static_salt_16bytes'  # Salt estático para fins de teste. Alterar para uma solução de salt persistente real.
    key = generate_key(password, salt)

    if os.path.exists(csv_path):
        with open(csv_path, mode='r') as file:
            reader = csv.reader(file)
            csv_data = "\n".join([",".join(row) for row in reader])
            encrypted_data = encrypt_data(csv_data.encode(), key)
            encrypted_data_b64 = b64encode(encrypted_data).decode('utf-8')  # Converte para Base64 para exibição

        # Salva o arquivo criptografado em uma pasta de backup
        if not os.path.exists(backup_folder):
            os.makedirs(backup_folder)
        backup_path = os.path.join(backup_folder, 'transferencias_criptografadas.bkp')
        with open(backup_path, 'wb') as backup_file:
            backup_file.write(encrypted_data)

        flash("Arquivo criptografado com sucesso!")
        return render_template('visualizar_csv.html', encrypted_data=encrypted_data_b64)
    else:
        flash("Arquivo CSV não encontrado.")
        return redirect(url_for('bemvindo'))


# Rota para descriptografar o CSV
@app.route('/descriptografar', methods=['POST'])
def descriptografar():
    backup_path = "backup/transferencias_criptografadas.bkp"

    # Obtém a senha fornecida pelo usuário
    password = request.form['password']
    salt = b'static_salt_16bytes'  # Salt estático para fins de teste. Alterar para uma solução de salt persistente real.
    key = generate_key(password, salt)

    if os.path.exists(backup_path):
        with open(backup_path, 'rb') as file:
            encrypted_data = file.read()
            try:
                decrypted_data = decrypt_data(encrypted_data, key)
                decrypted_data_str = decrypted_data.decode('utf-8')  # Convertendo de volta para string
                flash("Arquivo descriptografado com sucesso!")
                return render_template('visualizar_csv.html', encrypted_data=decrypted_data_str, confetti=True)  # Passa 'confetti=True' para ativar o efeito
            except Exception as e:
                flash("Erro ao descriptografar. Verifique sua senha.")
                return redirect(url_for('bemvindo'))
    else:
        flash("Backup não encontrado.")
        return redirect(url_for('bemvindo'))


# Tela de boas-vindas (protegida)
@app.route('/bemvindo')
def bemvindo():
    if 'user_id' not in session:
        flash('Você precisa fazer login para acessar esta página.')
        return redirect(url_for('login'))
    nome = session.get('nome')
    return render_template('bemvindo.html', nome=nome)


# Tela de login
@app.route('/')
def login():
    return render_template('login.html')


# Processa o login
@app.route('/login', methods=['POST'])
def fazer_login():
    email = request.form['email']
    senha = request.form['senha']

    conn = sqlite3.connect('banco.db')
    cursor = conn.cursor()
    cursor.execute("SELECT nome, senha FROM usuarios WHERE email = ?", (email,))
    usuario = cursor.fetchone()
    conn.close()

    if usuario and check_password_hash(usuario[1], senha):
        session['user_id'] = email
        session['nome'] = usuario[0]
        return redirect(url_for('bemvindo'))
    else:
        flash("Login falhou. Usuário ou senha incorretos.")
        return redirect(url_for('login'))


# Tela de registro
@app.route('/registro')
def registro():
    return render_template('registro.html')


# Processa o registro
@app.route('/registrar', methods=['POST'])
def registrar():
    nome = request.form['nome']
    email = request.form['email']
    senha = request.form['senha']

    conn = sqlite3.connect('banco.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE email = ?", (email,))
    usuario_existente = cursor.fetchone()

    if usuario_existente:
        flash('Email já registrado. Faça login ou use outro email.')
        return redirect(url_for('registro'))

    senha_hash = generate_password_hash(senha)
    cursor.execute("INSERT INTO usuarios (nome, email, senha) VALUES (?, ?, ?)", (nome, email, senha_hash))
    conn.commit()
    conn.close()

    flash("Registro bem-sucedido! Por favor, faça login.")
    return redirect(url_for('login'))


# Rota de logout
@app.route('/logout', methods=['POST'])
def logout():
    session.pop('user_id', None)
    session.pop('nome', None)
    flash('Logout realizado com sucesso.')
    return redirect(url_for('login'))


# Rota do jogo
@app.route('/jogo')
def jogo():
    if 'user_id' not in session:
        flash('Você precisa fazer login para acessar o jogo.')
        return redirect(url_for('login'))
    return render_template('jogo.html')

# Rota para visualizar o arquivo CSV puro
@app.route('/visualizar_csv')
def visualizar_csv():
    csv_path = "transferencias_ficticias.csv"

    if os.path.exists(csv_path):
        with open(csv_path, mode='r') as file:
            reader = csv.reader(file)
            csv_data = "\n".join([",".join(row) for row in reader])
        return render_template('visualizar_csv.html', encrypted_data=csv_data)
    else:
        flash("Arquivo CSV não encontrado.")
        return redirect(url_for('bemvindo'))

if __name__ == '__main__':
    criar_bd()  # Certifique-se de que o banco de dados seja criado ao iniciar
    app.run(debug=True)