from collections import OrderedDict

def filtrar_visuais(lista_visuais):
    # Converter a string de entrada em uma lista
    visuais = lista_visuais.split(", ")
    
    # TODO: Normalize e remova duplicatas usando um conjunto
    visuais_normalizados = [visual.strip().title() for visual in visuais]
    # TODO: Converta o conjunto de volta para uma lista ordenada:
    visuais_unicos = sorted(list(OrderedDict.fromkeys(visuais_normalizados)))

    
    # Unir a lista em uma string, separada por vírgulas
    return ", ".join(visuais_unicos)

# Capturar a entrada do usuário
entrada_usuario = input()

# Processar a entrada e obter a saída
saida = filtrar_visuais(entrada_usuario)
print(saida)