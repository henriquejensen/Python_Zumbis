number = -1

while 0 > number or number > 10:
    number = float(input("Digite uma nota entre 0 e 10: "))

    if 0 > number or number > 10:
        print("Valor invalido")
