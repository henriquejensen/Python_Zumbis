prime = int(input("Digite um numero inteiro: "))

yes = 0

for i in range(1, prime):
    if prime % i == 0:
        yes += 1

if yes == 1:
    print("O numero {} é primo".format(prime))

else:
    print("O numero {} não é primo".format(prime))
