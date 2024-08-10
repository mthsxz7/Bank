# Projeto de Controle de Finanças
=====================================

## Descrição do Projeto

O Projeto de Controle de Finanças é uma aplicação para gerenciar suas finanças pessoais de forma fácil e eficiente. Com ele, você pode criar contas, registrar transações, e acompanhar seu saldo em tempo real. A aplicação é ideal para quem deseja manter um controle rigoroso sobre seus gastos e receitas.

## Funcionalidades

* **Exibir Extrato**: Mostra o saldo atual da conta e todas as movimentações realizadas.
* **Realizar Depósito**: Permite adicionar fundos à conta.
* **Realizar Saque**: Permite retirar fundos da conta com controle de limite diário e número máximo de saques.
* **Criar Novo Usuário**: Cadastra novos usuários no sistema.
* **Criar Nova Conta**: Cria novas contas bancárias associadas a usuários existentes.
* **Listar Contas**: Exibe todas as contas cadastradas no sistema.

## Instalação

### Requisitos

* Python 3.9 ou superior
* pip (gerenciador de pacotes Python)

### Passos de Instalação

1. Clone o repositório: `git clone https://github.com/mthsxz7/Bank.git`
2. Navegue até o diretório do projeto: `cd Bank`
3. Instale as dependências: `pip install -r requirements.txt`
4. Execute a aplicação: `python bank.py`

## Contribuição

### Passos para Contribuir

1. Faça um fork do repositório.
2. Crie uma branch para sua contribuição (ex: `feature/nova-funcionalidade`): `git checkout -b nome-da-sua-branch`
3. Faça as alterações necessárias.
4. Adicione e faça commit das suas alterações: `git add .` e `git commit -m "Descrição das alterações"`
5. Envie suas alterações para o GitHub: `git push origin nome-da-sua-branch`
6. Abra um Pull Request para o repositório original.

### Guia de Estilo

* Use o padrão de codificação PEP 8.
* Use comentários para explicar o código.
* Teste suas alterações antes de enviar um pull request.
* Adicione documentação adequada para novas funcionalidades.

## Uso

### Interface de Linha de Comando

A aplicação é executada através da linha de comando. Você pode usar os seguintes comandos:

* `python bank.py` - Inicia a aplicação.
* `python bank.py --help` - Exibe a ajuda e os comandos disponíveis.

## Testes

Para garantir que a aplicação funcione corretamente, você pode rodar os testes incluídos. Use o seguinte comando:

```bash
pytest
```
