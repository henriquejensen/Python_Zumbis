#coding: utf-8

weather = float(input("Digite a temperatura em ºF (graus fahrenheit): "))

print("A temperatura de {fahr}ºF equivale a {celsius}ºC".format(fahr=weather, celsius=5*(weather-32)/9))
