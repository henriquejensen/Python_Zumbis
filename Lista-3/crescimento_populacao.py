#coding: utf-8

a = 80000
b = 200000
years = 0

while a <= b:
    a = a + 0.03*a
    b = b + 0.015*b
    years += 1

print("Serão necessários {} anos para que a população A ultrapasse a de B".format(years))
