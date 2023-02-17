#  Se achar necessario, faça import de outras bibliotecas





# Crie a função que será avaliada no exercício aqui
from socket import SOMAXCONN


a = int(input("primeiro numero: "))
b = int(input("segundo numero: "))

def op(num1, num2):
    soma = (num1 + num2)
    sub = (num1 - num2)
    if num2 == 0:
        div = 0
    else:
        div = (num1 / num2)
    mult = (num1 * num2)

    return soma, sub, div, mult
    

print(op(a, b))





# Teste a sua função aqui (caso ache necessário)











