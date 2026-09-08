# 💊 Sistema de Controle de Farmácia
Sistema web completo desenvolvido em **Python (Flask)** e **MySQL** para o gerenciamento eficiente de estoque e controle de medicamentos em estabelecimentos farmacêuticos. Projeto desenvolvido como parte do curso de Análise e Desenvolvimento de Sistemas.

## 🚀 Tecnologias e Ferramentas

- **Linguagem:** Python 3.x
- **Framework Web:** Flask
- **Banco de Dados:** MySQL / MySQL Workbench
- **Interface:** HTML5, CSS3
- **Controle de Versão:** Git e GitHub

---

## 📋 Pré-requisitos

Antes de iniciar, certifique-se de ter instalado em sua máquina:
- [Python](https://www.python.org/) (versão 3.8 ou superior)
- [Git](https://git-scm.com/)
- [MySQL Server / MySQL Workbench](https://dev.mysql.com/downloads/)

---

## 📂 Estrutura do Projeto

```text
sistema_farmacia
│
├── templates
│   └── index.html       # Interface de visualização e cadastro
├── .gitignore           # Arquivos ignorados pelo Git
├── app.py               # Lógica principal do Flask e rotas
└── README.md            # Documentação do projeto


⚙️ ''' Instalação e Configuração Passo a Passo
1. Clonar o Repositório
Abra o seu terminal ou prompt de comando e execute:

Bash
git clone [https://github.com/JVictorCastro-22/sistema_farmacia.git](https://github.com/JVictorCastro-22/sistema_farmacia.git)
cd sistema_farmacia
2. Instalar as Dependências
Instale o Flask e o conector oficial do MySQL para Python:

Bash
pip install flask mysql-connector-python
3. Configurar o Banco de Dados
Abra o seu MySQL Workbench, crie o schema do banco e a tabela necessária executando os comandos SQL abaixo:

SQL
CREATE DATABASE farmacia;

USE farmacia;

CREATE TABLE medicamentos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    lote VARCHAR(50) NOT NULL,
    quantidade INT NOT NULL,
    validade DATE NOT NULL
);
4. Ajustar as Credenciais
Abra o arquivo app.py no seu editor de código (como o VS Code) e verifique se as configurações de conexão com o MySQL correspondem ao seu ambiente local:

Python
conn = mysql.connector.connect(
    host="localhost",
    database="farmacia",
    user="root",
    password="SUA_SENHA_AQUI"  # Insira sua senha do MySQL se houver
)

🚀 Como Executar a Aplicação
1. Com o terminal na pasta raiz do projeto, execute o servidor Flask:
Bash
python app.py

2. O terminal exibirá um endereço local (geralmente http://127.0.0.1:5000).

3. Segure a tecla Ctrl e clique no link, ou copie e cole no seu navegador web de preferência para acessar o sistema.

👨‍💻 Autor
Desenvolvido por João Victor (JVictorCastro-22).
