# DoeMais 🕊️

**DoeMais** é uma aplicação desenvolvida em Python com interface gráfica feita em `Tkinter` e a utilização de `CRUD` para a manipulação de dados. Seu objetivo é gerenciar e registrar doações feitas por usuários, facilitando o controle e visualização dos dados de doação. O projeto foca em acessibilidade e praticidade, sendo ideal para organizações sociais, ONGs ou projetos de caridade.

---

## 📌 Funcionalidades

- Tela de **login** com autenticação simples.
- Registro de **doações** com informações como:
  - Nome do doador
  - Tipo da doação (alimentos, roupas, etc.)
  - Quantidade
  - Data
- Página principal com navegação entre seções.
- Armazenamento local das informações em um banco de dados SQLite (`doacoes.db`).
- Organização de código em módulos e reutilização de componentes.
- Relatório de adição de usuário, exclusão, edição, login e logout.

---

## 🖥️ Tecnologias Utilizadas

- **Python 3.13.3**
- **Tkinter** — Interface gráfica
- **SQLite** — Banco de dados leve e local

---

## 🗂️ Estrutura de Pastas

DoeMais-main/
│
├── main.py                 # Ponto de entrada da aplicação
├── doacoes.db              # Arquivo do banco SQLite
├── log_atividades.txt      # Arquivo de log das atividades
│
├── bd/                    # Módulos com funcionalidades específicas
│   ├──  banco.py                # Gerenciamento do banco de dados

├── paginas/                    # Módulos com funcionalidades específicas
│   ├── formulario.py           # Formulário de cadastro de doações
│   └── doacoes.py              # Tela de visualização das doações
├   └──login.py                 # Tela de login
├   └──principal.py             # Tela principal com menus
│




---

## ▶️ Como Executar

1. **Pré-requisitos:**
   - Python 3.13.3 instalado no sistema.

2. **Clone ou extraia o projeto:**
   ```bash
   git clone https://github.com/onunis/DoeMais.git
   # ou
   unzip DoeMais-main.zip

3. **Abra a pasta e abra com Visual Studio Code ou outra IDE**
4. **Dentro do Visual Studio Code, acesse a main do projeto e no canto superior direito, clique em "Executar Arquivo do Python"**


## 🔐 Login
O sistema utiliza uma verificação básica de login, apenas com usuário e senha sem verificações mais detalhadas.

## 🧠 Lógica do Sistema
A execução inicia por main.py, que chama a tela de login.

Após o login, o usuário é redirecionado à principal.py, onde há navegação para:

formulario.py – onde são cadastradas novas doações.

doacoes.py – onde é possível consultar as doações já registradas.

relatorio.py - onde é possível consultar adição de usuário, exclusão, edição, login e logout.

O módulo banco.py centraliza a lógica de acesso e manipulação do banco de dados SQLite.

## 🎯 Objetivo Acadêmico
Este projeto foi desenvolvido como parte de um trabalho acadêmico com o objetivo de aplicar conceitos de:

Programação orientada a objetos

Interfaces gráficas com Tkinter

Persistência de dados com SQLite

Modularização de código e boas práticas de organização

## 📸 Capturas de Tela
![image](https://github.com/user-attachments/assets/596a5f4a-264a-4cf2-afca-6336f30730af)
![image](https://github.com/user-attachments/assets/29585fc0-b629-4c72-8eb4-a831d486712e)
![image](https://github.com/user-attachments/assets/8fabd95e-1afe-45ee-9c28-14569ef2f9fb)
![image](https://github.com/user-attachments/assets/9802daea-cb90-4a9a-826a-ae6f45ec08c5)



## 👨‍💻 Autores
Nome: Guilherme de Araújo Nunes, Larissa Gabriel dos Santos e Gabriel Alves Campos

Curso: Análise e Desenvolvimento de Sistemas

Disciplina: Desenvolvimento Rápido de Aplicações em Python 2025.1

## 📄 Licença
Este projeto é de cunho acadêmico e livre para aprendizado.
