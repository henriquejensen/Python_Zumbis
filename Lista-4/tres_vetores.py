#coding: utf-8

import random

array = range(1,101)

arrayOne = []
arrayTwo = []
arrayThree = []

for i in range(10):
    arrayOne.append(random.choice(array))
    arrayTwo.append(random.choice(array))

for i in range(20):
    arrayThree.append(random.choice(arrayOne + arrayTwo))

print("Vetor 1 " + str(arrayOne))
print("Vetor 2 " + str(arrayTwo))
print("Vetor 3 " + str(arrayThree))
