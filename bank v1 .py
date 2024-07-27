# Função para exibir o extrato
def extrato(saldo, extrato_registro):
    print('\n================ EXTRATO ================')
    if not extrato_registro:
        print('Não foram realizadas movimentações.')
    else:
        print(extrato_registro)
    print(f'\nSaldo:\t\tR$ {saldo:.2f}')
    print('==========================================')

# Função para realizar depósito
def deposito(saldo, extrato_registro):
    valor_deposito = float(input('Digite o valor do depósito: R$ '))
    if valor_deposito <= 0:
        print('Digite um valor válido')
    else:
        saldo += valor_deposito
        extrato_registro += f'Depósito:\tR$ {valor_deposito:.2f}\n'
        print(f'Depósito de R$ {valor_deposito:.2f} efetuado com sucesso')
        print(f'Seu saldo atual é de R$ {saldo:.2f}')
    return saldo, extrato_registro

# Função para realizar saque
def saque(saldo, extrato_registro, limite, numero_saques, limite_saques):
    valor_saque = float(input('Qual o valor que você deseja sacar? R$ '))
    excedeu_saldo = valor_saque > saldo
    excedeu_limite = valor_saque > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print('Não é possível realizar a transação, dinheiro insuficiente')
    elif excedeu_limite:
        print('Valor do saque excede o limite')
    elif excedeu_saques:
        print('Número máximo de saques excedido')
    elif valor_saque > 0:
        saldo -= valor_saque
        extrato_registro += f'Saque:\t\tR$ {valor_saque:.2f}\n'
        numero_saques += 1
        print('Saque efetuado com sucesso.')
        print(f'Seu saldo atual é R$ {saldo:.2f}')
    else:
        print('Valor inválido para saque.')
    return saldo, extrato_registro, numero_saques

# Função para criar um novo usuário
def criar_usuario(usuarios):
    cpf = input('Informe o CPF (somente números): ')
    if any(usuario['cpf'] == cpf for usuario in usuarios):
        print('Usuário já cadastrado.')
        return
    nome = input('Informe o nome completo: ')
    data_nascimento = input('Informe a data de nascimento (dd-mm-aaaa): ')
    endereco = input('Informe o endereço: ')
    usuarios.append({'nome': nome, 'data_nascimento': data_nascimento, 'cpf': cpf, 'endereco': endereco})
    print('Usuário cadastrado com sucesso.')

# Função para criar uma nova conta
def criar_conta(agencia, numero_conta, usuarios, contas):
    cpf = input('Informe o CPF do usuário: ')
    usuario = next((user for user in usuarios if user['cpf'] == cpf), None)
    if usuario:
        contas.append({"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario, "saldo": 0.0})
        print('Conta criada com sucesso!')
    else:
        print('Usuário não encontrado.')

# Função para listar todas as contas
def listar_contas(contas):
    if not contas:
        print('Não há contas para listar.')
        return
    for conta in contas:
        print(f'Agência: {conta["agencia"]}, Conta: {conta["numero_conta"]}, Titular: {conta["usuario"]["nome"]}, Saldo: R$ {conta["saldo"]:.2f}')

# Saldo inicial e configuração do sistema
saldo = 0.0
extrato_registro = ""
limite = 500
numero_saques = 0
limite_saques = 3
usuarios = []
contas = []
agencia = "0001"

# Inicia o loop para verificar as opções
while True:
    print('\nMenu:')
    print('[1] Extrato')
    print('[2] Depósito')
    print('[3] Saque')
    print('[4] Nova conta')
    print('[5] Listar contas')
    print('[6] Novo usuário')
    print('[7] Sair')
    
    escolha = input('\nEscolha uma opção (1/2/3/4/5/6/7): ')
    
    if escolha.isdigit():
        escolha = int(escolha)
    else:
        print('Escolha uma opção válida')
        continue

    if escolha == 1:
        extrato(saldo, extrato_registro)
    elif escolha == 2:
        saldo, extrato_registro = deposito(saldo, extrato_registro)
    elif escolha == 3:
        saldo, extrato_registro, numero_saques = saque(saldo, extrato_registro, limite, numero_saques, limite_saques)
    elif escolha == 4:
        numero_conta = len(contas) + 1
        criar_conta(agencia, numero_conta, usuarios, contas)
    elif escolha == 5:
        listar_contas(contas)
    elif escolha == 6:
        criar_usuario(usuarios)
    elif escolha == 7:
        print('Saindo do sistema...')
        break
    else:
        print('Escolha uma opção válida')
