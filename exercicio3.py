#  Se achar necessario, faça import de outras bibliotecas





# Crie a função que será avaliada no exercício aqui
def soma_dos_aninhados(lista_de_listas):
    soma = 0
    for lista in lista_de_listas:
        soma += sum(lista)
    return soma
    
lista_de_listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
resultado = soma_dos_aninhados(lista_de_listas)
print(resultado)  # Output: 45

# Teste a sua função aqui (caso ache necessário)











