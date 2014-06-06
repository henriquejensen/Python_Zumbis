#coding: utf-8

number = int(input("Digite o numero: "))

number = list(str(number))
number.reverse()
number = ''.join(number)

print("O inverso de {} é {}".format(number, number))
