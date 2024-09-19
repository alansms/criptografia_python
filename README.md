# FIAP
**Disciplina**: Criptografia com Python  
**Professor**: Leonardo Ruiz Orabona

## Autores:
- **Alan de Souza Maximiano da Silva**  
  Email: rm557088@fiap.com.br  
  RM: 557088
- **Ana Carolina Martins da Silva**  
  Email: rm555762@fiap.com.br  
  RM: 555762
- **João Vitor Pires da Silva**  
  Email: rm556213@fiap.com.br  
  RM: 556213

# Projeto de Criptografia e Descriptografia de Arquivos com AES

## Descrição do Projeto

Este projeto foi desenvolvido para realizar a **criptografia e descriptografia de arquivos** utilizando o algoritmo **AES (Advanced Encryption Standard)**. Além de garantir a proteção dos arquivos, o projeto também implementa a criptografia de **senhas de usuários** para armazená-las de forma segura no banco de dados. O fluxo básico envolve a criptografia de arquivos localizados em uma pasta de origem, seu backup em uma pasta separada, e a posterior descriptografia com a senha correta.

## Funcionalidades

1. **Entrada da senha do usuário:** O usuário fornece uma senha que será usada tanto para criptografar/descriptografar arquivos quanto para criptografar a senha de acesso ao banco de dados.
2. **Criptografia de senha:** A senha do usuário é criptografada antes de ser armazenada no banco de dados, garantindo maior segurança.
3. **Acesso a uma pasta de arquivos:** O programa acessa uma pasta com arquivos que serão processados.
4. **Criptografia com AES:** Os arquivos na pasta são criptografados usando o protocolo AES.
5. **Backup dos arquivos criptografados:** Os arquivos criptografados são salvos em uma nova pasta separada como backup.
6. **Descriptografia:** O programa permite a descriptografia dos arquivos utilizando a senha correta fornecida pelo usuário.
7. **Validação de senha criptografada:** A senha criptografada é validada ao tentar descriptografar arquivos, garantindo que apenas usuários autorizados tenham acesso.

## Estrutura do Projeto

- **Parte 1:** Solicitação e entrada da senha do usuário.
- **Parte 2:** Criptografia da senha do usuário e armazenamento seguro no banco de dados.
- **Parte 3:** Acesso à pasta original e leitura dos arquivos a serem criptografados.
- **Parte 4:** Criptografia dos arquivos utilizando o algoritmo AES.
- **Parte 5:** Salvamento dos arquivos criptografados em uma pasta separada para backup.
- **Parte 6:** Descriptografia dos arquivos criptografados quando a senha correta for fornecida.
- **Parte 7:** Validação da senha criptografada e descriptografia dos arquivos.

## Tecnologias Utilizadas

- **Python 3.12**: Linguagem de programação utilizada para desenvolver o projeto.
- **Criptografia com AES (PyCryptodome)**: Utilizada tanto para criptografar os arquivos quanto para a criptografia de senhas.
- **SQLite**: Banco de dados utilizado para armazenar as senhas criptografadas dos usuários.
- **Flask**: Framework web para criar uma interface simples de interação com o usuário.

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/alansms/criptografia_python/edit/main/README.md

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/alansms/criptografia_python/edit/main/README.md
2. pip install -r requirements.txt
3. python app.py
4. http://localhost:5000
5. Diagrama:
 diagrama 

   
