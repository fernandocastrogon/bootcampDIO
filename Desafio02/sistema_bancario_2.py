from datetime import datetime
import pprint
contas = []
usuarios = []
numero_conta = 1
LIMITE_SAQUES = 3

def main():
    saldo = 0
    limite = 500
    extrato = []
    numero_saques = 0
    
    menu = """
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Criar usuário
    [5] Listar usuários
    [6] Criar conta
    [0] Sair

    => """

    while True:

        opcao = input(menu)

        if opcao == "1":
            valor_deposito = float(input("Digite o valor que deseja depositar: "))
            saldo, extrato = deposito(saldo, valor_deposito, extrato)
            
        elif opcao == "2":
            # Solicita o valor do saque ao usuário
            valor_saque = float(input("Digite o valor solicitado: "))

            # Chamada da função saque
            saldo, extrato = saque(
                saldo=saldo,
                valor_saque=valor_saque,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES
            )
        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)
        elif opcao == "4":
            criar_usuario(usuarios)
        elif opcao == "5":
            listar_usuario(usuarios)
        elif opcao == "6":
            criar_conta(contas, usuarios)
        elif opcao == "0":
            break

        else:
            print("Operação invalida, por favor selecione novamente a operação desejada.")

#Funcao Saque: 
#    A função saque deve reeber os argumentos apenas por nome(keyword only. Sugestão de argumentos: saldo, valor, extrato, limite, numero_saques, limite_saques) Sugestão de retorno
#    saldo e extrato.

def saque(*, saldo, valor_saque, extrato, limite, numero_saques, limite_saques):

    if numero_saques < LIMITE_SAQUES:
            
            if valor_saque > limite:
                print("Saque acima do limite de R$500,00")
            elif valor_saque > saldo:
                print("Saldo insuficiente em conta")
            else:
                saldo -= valor_saque
                numero_saques += 1
                print("Saque realizado com sucesso")
                horario_saque = datetime.now().strftime("%H:%M:%S")
                extrato.append(f"Saque de R$ {valor_saque:.2f} realizado as {horario_saque} \n")
    else:
        print("Limite diario de saques atingido")

    return saldo, extrato

#Função deposito:
#A função deposito deve recceber os argumentos apenas por posição(positional only). Sugestão de argumentos: saldo, valor, extrato. Sugestão de retorno: saldo e extrato.

def deposito(saldo, valor_deposito, extrato, /):
    
    
    if valor_deposito > 0:
        horario_deposito = datetime.now().strftime("%H:%M:%S")
        extrato.append(f"Deposito de R$ {valor_deposito:.2f} realizado as {horario_deposito}\n")
        saldo += valor_deposito
    else:
        print("Falha no deposito! O valor informado e invalido.")

    return saldo, extrato

#Função extrato:
# A função extrato deve receber os argumentos por posição e nome(positional only e keyword only). Argumentos posicionais: saldo, argumentos nomeados: extrato
 
def exibir_extrato(saldo, /, *, extrato):
    print("------EXTRATO------")
    print("\n".join(extrato))
    print(f"\n Saldo da conta: R${saldo:.2f}")

#Criar usuário
# O programa deve armazenas os usuários em uma lista, um usuário é composto por: nome, data de nascimento, cpf e endereço. O endereço é uma string ccom o formato: logradouro,
# nro - bairro - cidade/sigla estado. Deve ser armazenado somento os números do CPF. Não podemos cadastrar 2 usuários com o mesmo CPF.

def validaCPF():
    while True:
        cpf = input("Digite o CPF do usuário : ")
        if any(usuario[2] == cpf for usuario in usuarios):
            print("Este CPF já existe. Por favor, insira um CPF diferente.")
        else:
            return cpf
            break  # Sai do loop se o CPF for único

def criar_usuario(usuarios):
    dados_pessoais = []
    dados_pessoais.append(validaCPF())
    dados_pessoais.append(input("Digite o nome completo: "))
    dados_pessoais.append(input("Digite sua data de nascimento formato DD/MM/AAAA: "))
    dados_pessoais.append(input("Digite o endereço completo: "))
    usuarios.append(dados_pessoais)
    print('Usuário criado com sucesso')

#Listar usuário
    
def listar_usuario(usuarios):
    if not usuarios:
        print("Nenhum usuário cadastrado.")
        return
    usuarios_formatados = [
        f"Nome: {usuario[0]}, Data de Nascimento: {usuario[1]}, CPF: {usuario[2]}, Endereço: {usuario[3]}"
        for usuario in usuarios
    ]
    
    # Junta todas as strings com uma quebra de linha
    usuarios_str = "\n".join(usuarios_formatados)
    print("\nLista de Usuários:\n")
    print(usuarios_str)
    

#Criar Conta
# O programa deve armazenar contas em uma lista, uma conta é composta por: agência, número da conta e usuário. O número da conta é sequencial, iniciando em 1.
#   O número da agência é fixo: "0001". O usuário pode ter mais de uma conta, mas uma conta pertence a somente um usuário.
# Para vincular um usuário a uma conta, filtre a lista de usários buscando o número do CPF informado para cada usuário da lista.
    
def encontrar_indice_por_cpf(cpf):
    """Encontra o índice do usuário na lista com base no CPF."""
    for i, usuario in enumerate(usuarios):
        if usuario[2] == cpf:
            return i
    return -1

def criar_conta(contas, usuarios):
    
    global numero_conta
    while True:
        cpf = input("Digite o CPF: ")
        if cpf == "0":
            return
        if encontrar_indice_por_cpf(cpf) == -1:
            print ("CPF do usuário não cadastrado, tente novamente ou digite 0 para voltar ao menu")
            continue
        break
    contas.append("0001")
    contas.append(numero_conta)
    contas.append(usuarios[encontrar_indice_por_cpf(cpf)])
    print("Conta criada com sucesso")
    numero_conta += +1
    print(contas)

main()