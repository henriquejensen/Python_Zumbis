#coding: utf-8

def max_divisor(pnum1, pnum2):
    if pnum2 == 0:
        return pnum1

    else:
        return max_divisor(pnum2, pnum1%pnum2)


num1 = int(input("Digite o 1º numero inteiro: "))
num2 = int(input("Digite o 2º numero inteiro: "))

euclides = max_divisor(num1, num2)


print("O maximo divisor comum entre {} e {} é {}".format(num1, num2, euclides))
