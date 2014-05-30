cigarretes = float(input("Quantos cigarros voce fuma por dia: "))
years = float(input("A quantos anos voce ja fuma: "))

print("Voce ja perdeu {} dias da sua vida".format(round(cigarretes*10*years*365/3600, 1)))
