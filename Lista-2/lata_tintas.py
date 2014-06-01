#coding: utf-8

area = float(input("Digite o tamanho em metros da area a ser pintada: "))

if area % 3 == 0:
    liters = area / 3
else:
    liters = round(area / 3 + 1, 2)

if liters > 18:
    if liters % 18.0 == 0:
        quant = int(liters / 18.0)
    else:
        quant = int(liters / 18.0) + 1
else:
    quant = 1

print("Você devera comprar {} latas de tintas, pois ira usar {} litros de tinta".format(quant, liters))
