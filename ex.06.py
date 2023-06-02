while True:
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
    menu = int(input("Escolha:\n1 - Somar\n2 - Multiplicar\n3 - Subtrair\n4 - Divisão\n5 - Sair do Programa\nR:"))
    if menu == 1:
        soma = n1 +n2
        print(f"Soma: {soma}")
    if menu == 2:
        m = n1 * n2
        print(f"Multiplicar: {m}")
    if menu == 3:
        sub = n1 - n2
        print(f"Subtrair: {sub}")
    if menu == 4:
        div = n1 / n2
        print(f"Divisão: {div}")
    if menu == 5:
        break
