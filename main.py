while True:
    try:
        numero = input("Número: ")
        resultado = int(numero) % 2
        if resultado == 0:
            print(f"O número {numero} é par")
        else:
            print(f"O número {numero} é ímpar")

    except ValueError:
        if numero == 'quit':
            break
        else:
            print("Insira apenas números meu rei")

