#coding: utf-8

import random

choice = range(1, 101)
array = []

for i in range(10):
    array.append(random.choice(choice))

print("Os numero escolhidos foram {}".format(array))

array.sort()

print("O maior valor entre eles é {greater} e o menor é"
    " {smaller}".format(greater=array[9], smaller=array[0]))
