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
 
 Duas novas funções:
 

 

 
 
 Criar Conta

 O programa deve armazenar contas em uma lista, uma conta é composta por: agência, número da conta e usuário. O número da conta é sequencial, iniciando em 1.
   O número da agência é fixo: "0001". O usuário pode ter mais de uma conta, mas uma conta pertence a somente um usuário.
 Para vincular um usuário a uma conta, filtre a lista de usários buscando o número do CPF informado para cada usuário da lista.
   

 Listas contas'''
saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3

from datetime import datetime
import pprint

menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[4] Criar usuário
[5] Listar usuários
[0] Sair

=> """
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
 
def Extrato(saldo, /, *, extrato):
    print("------EXTRATO------")
    print("\n".join(extrato))
    print(f"\n Saldo da conta: {saldo:.2f}")


#Criar usuário
# O programa deve armazenas os usuários em uma lista, um usuário é composto por: nome, data de nascimento, cpf e endereço. O endereço é uma string ccom o formato: logradouro,
# nro - bairro - cidade/sigla estado. Deve ser armazenado somento os números do CPF. Não podemos cadastrar 2 usuários com o mesmo CPF.

usuarios = []

def criar_usuario():
    dados_pessoais = []

    dados_pessoais.append(input("Digite o nome completo"))
    dados_pessoais.append(input("Digite sua data de nascimento formato DD/MM/AAAA"))
    while True:
        cpf = input("Digite o CPF do usuário : ")
        # Verificar se o CPF já está na lista de usuários
        cpf_existe = any(usuario[2] == cpf for usuario in usuarios)
        
        if cpf_existe:
            print("Este CPF já existe. Por favor, insira um CPF diferente.")
        else:
            dados_pessoais.append(cpf)
            break  # Sai do loop se o CPF for único
    dados_pessoais.append(input("Digite o endereço completo"))
    usuarios.append(dados_pessoais)
    print('Usuário criado com sucesso')


#Listar usuário
    
def listar_usuario():
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
        Extrato(saldo, extrato=extrato)
    elif opcao == "4":
        criar_usuario()
    elif opcao == "5":
        listar_usuario()
    elif opcao == "0":
        break

    else:
        print("Operação invalida, por favor selecione novamente a operação desejada.")