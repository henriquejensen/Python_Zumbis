#coding: utf-8

lista = [1,2,3]

cont=0

while cont<3:
    lista[cont] = float(input("Digite o {}º lado do tringulo: ".format(cont+1)))
    cont+=1

if lista[0] + lista[1] > lista[2]:
    if lista[0] + lista[2] > lista[1]:
        if lista[2] + lista[1] > lista[0]:
            if lista[0] == lista[1] == lista[2]:
                print("OS valores podem formar um triangulo equilatero")
            elif lista[0] != lista[1] != lista[2]:
                print("OS valores podem formar um triangulo escaleno")
            else:
                print("OS valores podem formar um triangulo isósceles")
else:
    print("Os lados não formam um triangulo")
