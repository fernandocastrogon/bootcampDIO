def salvar_carro(marca, modelo, ano, placa):
    print(f"Carro inserido com sucesso!{marca}/{modelo}/{ano}/{placa}")


    # *args - passando uma tupla
    # **kwargs - passando um dicionario
    salvar_carro(**{"marca": "Fiat", "modelo": "Palio", "ano": 1999, "placa": "ABC-1234"})


def exibir_poema(data_extenso, *lista, **dicionario):
    texto = "\n".join(lista)
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in dicionario.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)

exibir_poema("Zen of Python", "Beautiful is better than ugly. ", autor="Tim Peters", ano=1999)


#def f(pos1, pos2, /, pos_or_kwd, *, kwd1,kwd2):

#Antes da "/" é apenas por posição
# Depois do "*" é apenas por keyworld
# Entre "/" e "*" pode ser posicional ou por keyworld


def somar(a, b):
    return a+b

def dividir(a, b):
    return a/b

def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operacao e de = {resultado}")

exibir_resultado(10, 10, somar)
exibir_resultado(20, 10, dividir)
