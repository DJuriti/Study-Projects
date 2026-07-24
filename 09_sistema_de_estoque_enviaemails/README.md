# 📦 Sistema de Estoque Automatizado

## 📖 Sobre o Projeto

Este projeto consiste em um sistema completo de gerenciamento de estoque desenvolvido em Python.

O sistema permite cadastrar, consultar, atualizar, remover e listar produtos armazenados em uma planilha Excel. Além disso, gera automaticamente um relatório em PDF e o envia por e-mail utilizando o protocolo SMTP.

O objetivo deste projeto foi praticar a integração entre diferentes bibliotecas Python, simulando uma automação utilizada em empresas para controle e compartilhamento de informações.

---

## 🚀 Funcionalidades

### 📦 Gerenciamento de Estoque

- Cadastrar produtos
- Consultar produtos
- Atualizar quantidade
- Atualizar preço
- Remover produtos
- Listar todos os produtos

### 📊 Integração com Excel

- Leitura da planilha
- Atualização automática dos dados
- Salvamento das alterações

### 📄 Geração de Relatórios

- Criação automática de relatório em PDF
- Organização das informações dos produtos
- Geração de relatório pronto para envio

### 📧 Envio Automático de E-mail

- Envio do relatório em PDF
- Anexo automático do arquivo
- Autenticação segura utilizando Senha de Aplicativo do Gmail
- Utilização de variáveis de ambiente (.env)

---

## 🛠️ Tecnologias Utilizadas

- Python 3
- OpenPyXL
- ReportLab
- SMTP (smtplib)
- EmailMessage
- Python-dotenv
- Pathlib

---

## 📁 Estrutura do Projeto

```text
Sistema_Estoque/
│
├── main.py
├── gerar_pdf.py
├── enviar_email.py
├── teste.xlsx
├── exemplo_relatorio.pdf
├── README.md
└── .gitignore
```

---

## 📚 Conceitos Praticados

- CRUD em Python
- Manipulação de planilhas Excel
- Geração de arquivos PDF
- Automação de envio de e-mails
- Variáveis de ambiente
- Manipulação de arquivos
- Organização de projetos
- Integração entre bibliotecas Python

---

## 🔒 Segurança

As credenciais utilizadas para envio de e-mails não ficam armazenadas no código-fonte.

As informações sensíveis são protegidas através de um arquivo `.env`, evitando a exposição de dados pessoais no GitHub.

---

## 🎯 Objetivos de Aprendizagem

Durante este projeto foram praticados conceitos importantes como:

- Manipulação de planilhas Excel
- Geração de relatórios em PDF
- Automação de processos
- Envio de e-mails utilizando SMTP
- Utilização de variáveis de ambiente
- Organização e modularização de projetos Python

---

## 👨‍💻 Autor

Desenvolvido por **Davi** como parte da minha jornada de estudos em Python, automação e desenvolvimento de software.
