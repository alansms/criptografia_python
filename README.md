FIAP
aula_leonardo_fiap # criptografia_python 
Professor: Leonardo Ruiz Orabona

# Alan de Souza Maximiano da Silva
Email: rm557088@fiap.com.br
RM:557088

# Ana Carolina Martins da Silva
Email: rm555762@fiap.com.br
RM:555762

# João Vitor Pires da Silva
Email: rm556213@fiap.com.br
RM:556213


# Projeto de Criptografia e Descriptografia de Arquivos com AES

## Descrição do Projeto

Este projeto foi desenvolvido para realizar a criptografia e descriptografia de arquivos utilizando o algoritmo AES (Advanced Encryption Standard). O programa acessa uma pasta com arquivos que precisam ser criptografados, realiza a criptografia e, em seguida, salva os arquivos criptografados em uma pasta de backup. Além disso, o programa permite a descriptografia dos arquivos previamente criptografados.

## Funcionalidades

1. **Entrada da senha do usuário:** O usuário deve fornecer uma senha que será usada para a criptografia e a descriptografia dos arquivos.
2. **Acesso a uma pasta de arquivos:** O programa acessa uma pasta com arquivos que serão processados.
3. **Criptografia com AES:** Os arquivos na pasta são criptografados usando o protocolo AES.
4. **Backup dos arquivos criptografados:** Os arquivos criptografados são salvos em uma nova pasta separada como backup.
5. **Descriptografia:** O programa permite a descriptografia dos arquivos usando a senha fornecida.

## Estrutura do Projeto

- **Parte 1:** Solicitação e entrada da senha do usuário.
- **Parte 2:** Acesso à pasta original e leitura dos arquivos a serem criptografados.
- **Parte 3:** Criptografia dos arquivos utilizando o algoritmo AES.
- **Parte 4:** Salvamento dos arquivos criptografados em uma pasta separada para backup.
- **Parte 5:** Descriptografia dos arquivos criptografados quando a senha correta for fornecida.

## Tecnologias Utilizadas

- **Python 3.12**: Linguagem de programação utilizada para desenvolver o projeto.
- **Criptografia com AES (PyCryptodome)**: Utilizado para realizar a criptografia e descriptografia dos arquivos.
- **Flask**: Framework web para criar uma interface simples de interação com o usuário.

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/alansms/criptografia_python/edit/main/README.md
2. pip install -r requirements.txt
3. python app.py
4. http://localhost:5000
   
