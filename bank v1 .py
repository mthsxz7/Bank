# Verifica o saldo atual
saldo = 0

# Variáveis para armazenar os contadores
cont_depositos = 0
cont_saques = 0

# Exibindo o menu inicial
print('\nMenu:')
print('[1] Extrato')
print('[2] Depósito')
print('[3] Saque')
print('[4] Sair')

# Inicia o loop para verificar as opções
while True:
    opcao = int(input('Escolha uma opção (1/2/3/4): '))

    # Começa a verificar a escolha do usuário
    if opcao == 1:
        print('Seu saldo atual é R$ {:.2f}'.format(saldo))

    elif opcao == 2:
        valor_deposito = float(input('Digite o valor do depósito: R$ '))
        if valor_deposito <= 0:
            print('Digite um valor válido')
        else:
            saldo += valor_deposito
            cont_depositos += 1  # contador de depósitos
            print('Depósito de {:.2f} efetuado com sucesso'.format(valor_deposito))
            print('Seu saldo atual é de {:.2f}'.format(saldo))

    elif opcao == 3:
        valor_saque = float(input('Qual o valor do saque? R$ '))
        if valor_saque > saldo:
            print('Não é possível realizar a transação, dinheiro insuficiente')
        else:
            saldo -= valor_saque
            cont_saques += 1  # contador de saques
            print('Saque efetuado com sucesso.')
            print('Seu saldo atual é {:.2f}'.format(saldo))

    elif opcao == 4:
        print('Fechando o programa...')
        break  # Encerra o loop assim que o usuário escolhe a opção 4

    else:
        print('Opção inválida. Digite uma opção válida (1/2/3/4)')

# Exibindo o total de operações realizadas na conta
print(f'Total de depósitos realizados: {cont_depositos}')
print(f'Total de saques realizados: {cont_saques}')

