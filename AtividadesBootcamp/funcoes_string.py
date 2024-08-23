import math

nome = "fErnAndO"

#altera toda string para letra minuscula
print(nome.lower())

#altera toda string para letra maiuscula
print(nome.upper())

#altera toda string para letra minuscula com a primeira letra maiuscucla
print(nome.title())


texto = "       Hello world! "

#corta o espaco em branco do inicio e do fim da string
print(texto.strip() + ".")

#corta o espaco em branco do lado esquerdo 
print(texto.lstrip() + ".")

#remove todo espaco em branco do lado direito
print(texto.rstrip() + ".")

menu = "Python"

#Centraliza a string completando o lado esquerdo e o direito com o caraceter a sua escolha
print(menu.center(14, "-"))

#Adiciona a string de sua escolha apos cada caracter da string selecionada
print(".".join(menu))


#Metodo Format

nome = "Fernando"
idade = 28
profissao = "Programador"
linguagem = "Python"

dados = {"nome": "Fernando", "idade": 28, "profissao": "Programador", "linguagem": "Python"}


print("Ola, me chamo {3}. Eu tenho {2} anos de idade, trabalho como {1} e estou matriculado no curso de {0}"
      .format(linguagem, profissao, idade,nome))

print("Ola, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}"
 .format(**dados))

#print("Ola, me chamo{nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}"
#      .format(nome=nome, idade=idade, profissao=profissao,linguagem=linguagem))


#f-string

print(f"Ola, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.")

PI = math.pi
print(f"Valor de PI: {PI:.2f} ")
# "Valor de PI: 3.14"


#Fatiamento de string

nome = "Fernando Castro Goncalves"

print(nome[0])
#"F"

print(nome[:8])
#"Fernando"

print(nome[9:15])
#"Castro"

print(nome[9:15:2])
#Csr

print(nome[::-1])
#sevlacnoG ortsaC odnanreF (Espelhamento)

#String multiplas linhas
print(f'''
 Ola meu nome e {nome}.
 Estou aprendendo Python
'''
)

