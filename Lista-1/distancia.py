distance = float(input("Qual a distancia que sera percorrida: "))
velocity = float(input("Qual a velocidade media: "))

time = int(distance/velocity)

minutes = (distance/velocity)%1*60

print("O tempo de viagem sera de {tim} horas e {min} minutos".format(tim=time, min=round(minutes, 2)))
