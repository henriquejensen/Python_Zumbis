#coding: utf-8

import random

arrayPar = []
arrayImpar = []
luck = []

array = range(1,101)

for i in range(20):
    choice = random.choice(array)
    luck.append(choice)
    if choice%2 == 0:
        arrayPar.append(choice)
    else:
        arrayImpar.append(choice)

print("Numeros sorteados " + str(luck))
print("Os numeros pares " + str(arrayPar))
print("Os numeros impares " + str(arrayImpar))
