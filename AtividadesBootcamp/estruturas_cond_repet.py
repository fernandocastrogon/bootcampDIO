''' 
    Blocos em Python: Adicionamos 4 novos espacos em branco para cada bloco de indentacao
    Iniciamos blocos de metodos, estruturas com dois pontos :
'''
def sacar(valor):
    saldo = 500

    if saldo >= valor:
        print("Valor sacado!")

sacar(100)

#If ternario

saldo = 2000
saque = 500

status = "Sucesso" if saldo >= saque else "Falha"

#Estruturas de repeticao


#for

texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
print() #executa uma quebra de 

''' 
    range - Funcao para produzir uma sequencia de numeros inteiros a partir de um inicio(INCLUSIVO)
    para um fim (exclusivo). Se usarmos range(i,j) sera produzido:
    i, i+1, i+2, i+3,....-j-1
    Ela recebe 3 argumentos - stop(obrigatorio), start(opcional) e step(opcional)
'''

list(range(4))
# [0, 1, 2, 3]

# exibi a tabuada do 5
for numero in range(0, 51, 55):
    print(numero, end="")
# 0 5 10 15 20 25 30 35 40 45 50


#while - Utilizado quando nao sabemos a quantidade que sera repetida

opcao = -1

while opcao != 0:
    opcao = int(input("[1] Sacar \n [2] Extrato \n [0] Sair \n: "))
    if opcao == 1:
        print("Sacando....")
    elif opcao == 2:
        print("Exibindo o extrato")
print("Obrigado por usar nosso sistema, ate logo")


#comando break - sai da estrutura de repeticao, cortando o laco
#comando continue - pula uma repeticao

#exibi apenas os numeros impares de 0 a 99, utilizando o continue
for numero in range(100):
    if numero % 2 == 0:
        continue
    print(numero, end="")