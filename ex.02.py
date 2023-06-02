pares = 0

while True:
    num = int(input("digite um número: "))
    if num == 0:
        print('Você digitpu [0], parou o programa.')
        print("A soma dos numeros pares é:", pares)
        break
    elif num % 2 == 0:
        pares += num
        f = str(input('Deseja continuar?[S/N]:'))

        if f.upper() == 'N':
         print("A soma dos numeros pares é:", pares)
         break