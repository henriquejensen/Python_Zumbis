#coding: utf-8

weight = float(input("João, digite o valor do peixe que pescou em quilos(kg): "))

over = weight - 50
penalty = over * 4

if over <= 0:
    print("João, você não tem nenhuma divida")
else:
    print("João, você tem uma divida de R${div} pelo excesso de {peso}kg".format(div=penalty, peso=over))
