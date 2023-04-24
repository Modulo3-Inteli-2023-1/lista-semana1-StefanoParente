#  Se achar necessario, faça import de outras bibliotecas





# Crie a função que será avaliada no exercício aqui
def tem_duplicados(lista):
    lista_vazia = []
    soma = 0
    for lista1 in lista:
        lista2 = lista1
        lista_vazia.append(lista2)
        if lista_vazia.count(lista1) > 1:
            soma = 1
        else:
            soma = 0
    if soma == 1:
        return True
    else:
        return False                

# Teste a sua função aqui (caso ache necessário)











