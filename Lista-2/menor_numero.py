#coding: utf-8

array = []

for i in range(0,3):
    num = float(input("Digite o {}º numero: ".format(i+1)))
    array.append(num)

array.sort()

print("O menor numero entre eles é o {}".format(array[0]))
print("O maior numero entre eles é o {}".format(array[2]))
