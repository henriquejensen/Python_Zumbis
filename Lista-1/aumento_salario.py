pay = float(input("Digite seu salario: "))
increase = float(input("Digite a porcentagem do aumento: "))

print("Voce obteve R${sal} de aumento".format(sal=pay*increase/100))
print("Seu novo salario sera de R${sal}".format(sal=pay + pay*increase/100))
