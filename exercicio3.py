#  Se achar necessario, faça import de outras bibliotecas





# Crie a função que será avaliada no exercício aqui
def soma_dos_aninhados(lista_de_listas):
    lista_vazia = []
    t = 0
    soma = 0
    for lista in lista_de_listas:
        t = lista
        lista_vazia.append(t)
    for lista1 in lista_vazia:
        soma += sum(lista1)
    return soma
    

# Teste a sua função aqui (caso ache necessário)











