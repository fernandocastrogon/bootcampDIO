'''
Fomos contratados por um grande banco para desenvolver seu novo sistema.
Esse banco deseja modernizar suas operacoes e para isso escolheu a linguagem Python.
Para a primeira versao do sistema devemos implementar apenas 3 operacoes:

Deposito:
    Deve ser possivel depositar valores positivos para a minha conta bancaria.
    A v1 do projeto trabalha apenas com 1 usuario, dessa forma nao precisamos nos preocupar
    em identificar qual e o numero da agencia e conta bancaria. Todos os depositos devem ser
    armazenados em uma variavel e exibidos na operacao de extrato

Saque:
    O sistema deve permitir realizar 3 saques diarios com limite maximo de R$500,00 por saque.
    Caso o usuario nao tenha saldo em conta, o sistema deve exibir uma mensagem informando que 
    nao sera possivel sacar o dinheiro por falta de saldo. Todos os saques devem ser armazenados
    em uma variavel e exibidos na operacao de extrato
    
Extrato
    Essa operacao deve listar todos os depositos e saques realizados na conta.
    No fim da listagem deve ser exibido o saldo atual da conta.
    Os valores devem ser exibidor utilizando o formato R$ XXX.XX, exemplo:
    1500.45 = R$ 1500.45


'''
from datetime import datetime

menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3


while True:

    opcao = input(menu)

    if opcao == "1":
       
        deposito = float(input("Digite o valor que deseja depositar: "))
        if deposito > 0:
            horario_deposito = datetime.now().strftime("%H:%M:%S")
            extrato.append(f"Deposito de R$ {deposito:.2f} realizado as {horario_deposito}\n")
            saldo += deposito
        else:
            print("Falha no deposito! O valor informado e invalido.")
       
    elif opcao == "2":
        if numero_saques < LIMITE_SAQUES:
            saque = float(input("Digite o valor que deseja sacar: "))

            if saque > limite:
                print("Saque acima do limite de R$500,00")
            elif saque > saldo:
                print("Saldo insuficiente em conta")
            else:
                saldo -= saque
                numero_saques += 1
                print("Saque realizado com sucesso")
                horario_saque = datetime.now().strftime("%H:%M:%S")
                extrato.append(f"Saque de R$ {saque:.2f} realizado as {horario_saque} \n")
        else:
            print("Limite diario de saques atingido")
    elif opcao == "3":
        print("------EXTRATO------")
        print("\n".join(extrato))
        print(f"\n Saldo da conta: {saldo}")
    elif opcao == "0":
        break

    else:
        print("Operacao invalida, por favor selecione novamente a operacaoo desejada.")