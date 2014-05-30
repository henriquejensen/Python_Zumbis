price = float(input("Digite o preco da mercadoria: "))
rebate = float(input("Digite o percentual de desconto: "))

print("O valor do desconto R${value}".format(value=price*rebate))
print("O valor a ser pago R${value}".format(value=price - price*rebate))
