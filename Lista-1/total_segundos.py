days = int(input("Digite a quantidade de dias: "))
hours = int(input("Digite a quantidade de horas: "))
minutes = int(input("Digite a quantidade de minutos: "))
seconds = int(input("Digite a quantidade de segundos: "))

total_seconds = days*60*60*24 + hours*60*60 + minutes*60 + seconds

print("O total em segundos eh {sec}".format(sec = total_seconds))
