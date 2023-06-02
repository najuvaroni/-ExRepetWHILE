while True:
    sexo = str(input('Digite o seu genero [M/F]: '))

    if sexo.upper() != "M" and sexo != 'F':
        print("Escrita errada!")
        sexo= str(input('Digite seu genero [M/F]: '))
    else:
        break