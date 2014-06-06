# coding: utf-8


def divisors():
    aux = number
    for i in range(2, number):
        while aux % i == 0:
            arrayDivisors.append(i)
            aux /= i


def prime(prime):
    yes = 0
    for i in range(1, prime):
        if prime % i == 0:
            yes += 1

    if yes == 1:
        arrayPrime.append(prime)

number = int(input("Digite um numero inteiro positivo: "))
arrayDivisors = []
arrayPrime = []
divisors()

cont = 0
while cont < len(arrayDivisors):
    prime(arrayDivisors[cont])
    cont += 1

if len(arrayPrime) == 0:
    print(
        "O numero {} é primo".format(number))

else:
    print("Os cofatores de {num} são {lista}".format(
        num=number, lista=arrayPrime))
