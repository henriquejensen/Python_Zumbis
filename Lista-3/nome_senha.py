#coding: utf-8

accept = False

name = input("Digite seu nome: ")

while accept == False:
    keyword = input("Digite sua senha: ")

    if name in keyword:
        print("Sua senha não pode conter seu nome, repita a operação")
    else:
        accept = True
        print("That's right")
