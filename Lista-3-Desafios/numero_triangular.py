number = int(input("Digite um numero: "))

first, second, third = 0, 0, 0

for i in range(1, 10000):
    if number % i == 0:
        if number % (i + 1) == 0:
            if number % (i + 2) == 0:
                first = i
                second = i + 1
                third = i + 2


if first != 0 and first * second * third == number:
    print("O {} é triangular de {}*{}*{}".format(number, first, second, third))
else:
    print("O {} não é triangular".format(number))
