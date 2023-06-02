soma = 0
qnt = 0
while True:
    nota = float(input('Digite a nota: '))
    qnt += 1
    soma += nota
    f = str(input('Deseja continuar?[S/N]:'))
    if nota < 0:
        print('O número é negativo')
        media = soma / qnt
        print('A média é:', media)
        break
    elif f.upper() == 'N':
        media = soma/ qnt
        print('A média é: ', media)
        break