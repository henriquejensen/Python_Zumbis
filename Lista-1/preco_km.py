distance = float(input("Digite a quantidade de quilometros que ira percorrer com o carro: "))
days = int(input("Digite a quantidade de dias que ficara com o carro: "))

print("Voce ira pagar R${price} para usar o carro".format(price=days*60+distance*0.15))
