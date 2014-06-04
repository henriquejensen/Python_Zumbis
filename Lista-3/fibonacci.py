#coding: utf-8

def fibonacci(number):
    if number == 1 or number == 0:
        return 1

    return fibonacci(number-1) + fibonacci(number-2)

number = int(input("Digite um numero inteiro para o calculo do fibonacci: "))
print("O fibonacci de {num} é {fibo}".format(num=number, fibo=fibonacci(number)))
