num = 0
while True:
    num = int(input('Digite o número:'))
    if num < 0:
     print('O número é negativo')
     break
    elif num == 999:
     break
    else:
     f = str(input('Deseja continuar?[S/N]:'))
     if f.upper() == 'N':
      break