def exibir_mensagem_erro(mensagem):
    print(f"Erro: {mensagem}")

def extrato(saldo, extrato_registro):
    """
    Exibe o extrato da conta, mostrando o saldo e as movimentações realizadas.

    :param saldo: Saldo atual da conta.
    :param extrato_registro: Registro das movimentações realizadas.
    """
    print('\n================ EXTRATO ================')
    if not extrato_registro:
        print('Não foram realizadas movimentações.')
    else:
        print(extrato_registro)
    print(f'\nSaldo:\t\tR$ {saldo:.2f}')
    print('==========================================')

def obter_valor_positivo(mensagem):
    """
    Solicita um valor positivo ao usuário e garante que a entrada seja válida.

    :param mensagem: Mensagem a ser exibida para o usuário.
    :return: Valor positivo fornecido pelo usuário.
    """
    while True:
        try:
            valor = float(input(mensagem))
            if valor <= 0:
                print("O valor deve ser positivo.")
            else:
                return valor
        except ValueError:
            print("Entrada inválida. Digite um número válido.")

def deposito(saldo, extrato_registro):
    """
    Realiza um depósito na conta.

    :param saldo: Saldo atual da conta.
    :param extrato_registro: Registro das movimentações realizadas.
    :return: Novo saldo e registro atualizado do extrato.
    """
    valor_deposito = obter_valor_positivo('Digite o valor do depósito: R$ ')
    saldo += valor_deposito
    extrato_registro += f'Depósito:\tR$ {valor_deposito:.2f}\n'
    print(f'Depósito de R$ {valor_deposito:.2f} efetuado com sucesso')
    print(f'Seu saldo atual é de R$ {saldo:.2f}')
    return saldo, extrato_registro

def saque(saldo, extrato_registro, limite, numero_saques, limite_saques):
    """
    Realiza um saque da conta com verificações de limite.

    :param saldo: Saldo atual da conta.
    :param extrato_registro: Registro das movimentações realizadas.
    :param limite: Limite máximo para saques.
    :param numero_saques: Número atual de saques realizados.
    :param limite_saques: Limite máximo de saques por dia.
    :return: Novo saldo, registro atualizado do extrato e número de saques realizados.
    """
    valor_saque = obter_valor_positivo('Qual o valor que você deseja sacar? R$ ')
    excedeu_saldo = valor_saque > saldo
    excedeu_limite = valor_saque > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        exibir_mensagem_erro('Não é possível realizar a transação, dinheiro insuficiente')
    elif excedeu_limite:
        exibir_mensagem_erro('Valor do saque excede o limite')
    elif excedeu_saques:
        exibir_mensagem_erro('Número máximo de saques excedido')
    elif valor_saque > 0:
        saldo -= valor_saque
        extrato_registro += f'Saque:\t\tR$ {valor_saque:.2f}\n'
        numero_saques += 1
        print('Saque efetuado com sucesso.')
        print(f'Seu saldo atual é R$ {saldo:.2f}')
    else:
        exibir_mensagem_erro('Valor inválido para saque.')
    return saldo, extrato_registro, numero_saques

def criar_usuario(usuarios):
    """
    Cria um novo usuário no sistema.

    :param usuarios: Lista de usuários cadastrados.
    """
    cpf = input('Informe o CPF (somente números): ')
    if any(usuario['cpf'] == cpf for usuario in usuarios):
        exibir_mensagem_erro('Usuário já cadastrado.')
        return
    nome = input('Informe o nome completo: ')
    data_nascimento = input('Informe a data de nascimento (dd-mm-aaaa): ')
    endereco = input('Informe o endereço: ')
    usuarios.append({'nome': nome, 'data_nascimento': data_nascimento, 'cpf': cpf, 'endereco': endereco})
    print('Usuário cadastrado com sucesso.')

def criar_conta(agencia, numero_conta, usuarios, contas):
    """
    Cria uma nova conta bancária para um usuário existente.

    :param agencia: Agência da conta.
    :param numero_conta: Número da conta.
    :param usuarios: Lista de usuários cadastrados.
    :param contas: Lista de contas cadastradas.
    """
    cpf = input('Informe o CPF do usuário: ')
    usuario = next((user for user in usuarios if user['cpf'] == cpf), None)
    if usuario:
        contas.append({"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario, "saldo": 0.0})
        print('Conta criada com sucesso!')
    else:
        exibir_mensagem_erro('Usuário não encontrado.')

def listar_contas(contas):
    """
    Lista todas as contas cadastradas.

    :param contas: Lista de contas cadastradas.
    """
    if not contas:
        print('Não há contas para listar.')
        return
    for conta in contas:
        print(f'Agência: {conta["agencia"]}, Conta: {conta["numero_conta"]}, Titular: {conta["usuario"]["nome"]}, Saldo: R$ {conta["saldo"]:.2f}')

def menu():
    """
    Exibe o menu principal e retorna a escolha do usuário.
    """
    print('\nMenu:')
    print('[1] Extrato')
    print('[2] Depósito')
    print('[3] Saque')
    print('[4] Nova conta')
    print('[5] Listar contas')
    print('[6] Novo usuário')
    print('[7] Sair')
    return input('\nEscolha uma opção (1/2/3/4/5/6/7): ')

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
    escolha = menu()
    
    if escolha.isdigit():
        escolha = int(escolha)
    else:
        exibir_mensagem_erro('Escolha uma opção válida')
        continue

    if escolha == 1:
        extrato(saldo, extrato_registro)
    elif escolha == 2:
        saldo, extrato_registro = deposito(saldo, extrato_registro)
    elif escolha == 3:
        saldo, extrato_registro, numero_saques = saque(saldo, extrato_registro, limite, numero_saques, limite_saques)
    elif escolha == 4:
        criar_conta(agencia, len(contas) + 1, usuarios, contas)
    elif escolha == 5:
        listar_contas(contas)
    elif escolha == 6:
        criar_usuario(usuarios)
    elif escolha == 7:
        print('Saindo...')
        break
    else:
        exibir_mensagem_erro('Escolha uma opção válida')
