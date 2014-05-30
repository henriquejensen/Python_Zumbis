#coding: utf-8

temp = float(input("Digite a temperatura em ºC (graus celsius): "))

print(u"A temperatura de {celsius}ºC eh o mesmo que {fahr}ºF".format(celsius=temp, fahr=temp*9/5 + 32))
