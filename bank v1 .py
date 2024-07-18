'''By: mthsxz7 '''

def extrato(saldo):
    print(f'Seu saldo atual é R$ {saldo:.2f}')

def deposito(saldo):
    valor_deposito = float(input('Digite o valor do depósito: R$ '))
    if valor_deposito <= 0:
        print('Digite um valor válido')
    else:
        saldo += valor_deposito
        print(f'Depósito de R$ {valor_deposito:.2f} efetuado com sucesso')
        print(f'Seu saldo atual é de R$ {saldo:.2f}')
    return saldo

def saque(saldo):
    print(f'Seu saldo atual é de R$ {saldo:.2f}')
    valor_saque = float(input('Qual o valor que você deseja sacar? R$ '))
    if valor_saque > saldo:
        print('Não é possível realizar a transação, dinheiro insuficiente')
    else:
        saldo -= valor_saque
        print('Saque efetuado com sucesso.')
        print(f'Seu saldo atual é R$ {saldo:.2f}')
    return saldo

# Saldo inicial
saldo = 0.0

# Inicia o loop para verificar as opções
while True:
    print('\nMenu:')
    print('[1] Extrato')
    print('[2] Depósito')
    print('[3] Saque')
    print('[4] Sair')
    escolha = int(input('Escolha uma opção (1/2/3/4): '))
    
    if escolha == 1:
        extrato(saldo)
    elif escolha == 2:
        saldo = deposito(saldo)
    elif escolha == 3:
        saldo = saque(saldo)
    elif escolha == 4:
        print('Saindo do sistema...')
        break
    else:
        print('Escolha uma opção válida')