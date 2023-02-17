#  Se achar necessario, faça import de outras bibliotecas





# Crie a função que será avaliada no exercício aqui
def tem_duplicados(lista):
    return len(lista) != len(set(lista))
    
lista = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9]
resultado = tem_duplicados(lista)
print(resultado)  # Output: True




# Teste a sua função aqui (caso ache necessário)











