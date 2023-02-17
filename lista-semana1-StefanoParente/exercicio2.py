#  Se achar necessario, faça import de outras bibliotecas




# Crie a função que será avaliada no exercício aqui
a = list(map(int, input("\nColoque os numeros: ").strip().split()))
nova_lista = []
j = 0
for i in range(0 , len(a)):
    j += a[i]
    nova_lista.append(j)

print(nova_lista)

# Teste a sua função aqui (caso ache necessário)











