preco = 0
nome = " "
caro = 0
pcaro = ' '
soma = 0
while True:
    nome = str(input("Digite o nome do produto: "))
    preco = float(input('Informe o preço: '))
    soma += preco

    if preco > caro:
        pcaro = nome
        caro = preco

    f = str(input('Deseja continuar?[S/N]:'))
    if f.upper() == 'N':
        break

print("Total gasto na compra: ", soma)
print("Nome do produto mais caro: ", pcaro)

