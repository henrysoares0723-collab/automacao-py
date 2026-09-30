# 🤖 Automação de Cadastro de Produtos

Projeto desenvolvido em Python com o objetivo de automatizar o cadastro de produtos em uma plataforma web a partir de dados armazenados em um arquivo CSV.

Este projeto faz parte dos meus estudos em Python e foi desenvolvido para praticar conceitos de automação, manipulação de dados e estruturas de repetição.

## 📌 Sobre o projeto

A aplicação lê os produtos armazenados no arquivo `produtos.csv` e utiliza a biblioteca PyAutoGUI para preencher automaticamente os campos de cadastro em uma página web.

O objetivo é evitar o preenchimento manual de cada produto, utilizando Python para realizar as ações repetitivas.

O projeto também foi uma forma de colocar em prática conceitos que estou aprendendo durante meus estudos de programação.

## ⚙️ Como funciona

O processo de automação segue basicamente estas etapas:

1. Abre o navegador Google Chrome.
2. Acessa a página de login da plataforma.
3. Realiza o login.
4. Lê os dados do arquivo `produtos.csv`.
5. Percorre cada produto utilizando um loop `for`.
6. Preenche os campos do formulário automaticamente.
7. Utiliza a tecla `Tab` para navegar entre os campos.
8. Envia o cadastro.
9. Repete o processo para os demais produtos.

### Fluxo simplificado

```text
produtos.csv
     ↓
Pandas
     ↓
Leitura dos dados
     ↓
Loop pelos produtos
     ↓
PyAutoGUI
     ↓
Preenchimento do formulário
     ↓
Cadastro dos produtos
