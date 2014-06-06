# coding: utf-8

bought = int(input("Digite o valor da conta em R$: "))
pay = int(input("Informe o valor do pagamento em R$: "))
bill = pay - bought

jaguar, monkey, parrot, egret, turtle, bird = 0, 0, 0, 0, 0, 0


if bill >= 50:
    jaguar = int(bill / 50)
    bill = bill - 50 * jaguar

if bill >= 20:
    monkey = int(bill / 20)
    bill -= 20 * monkey

if bill >= 10:
    parrot = int(bill / 10)
    bill -= 10 * parrot

if bill >= 5:
    egret = int(bill / 5)
    bill -= 5 * egret

if bill >= 2:
    turtle = int(bill / 2)
    bill -= 2 * turtle

bird = bill


print("Seu troco sera de:\n {fifty} notas de R$50,00\n {twenty} notas de R$20,00\n "
      "{ten} notas de R$10,00\n {five} notas de R$5,00\n "
      "{two} notas de R$2,00\n {one} notas de R$1,00".format(fifty=jaguar, twenty=monkey,
                                                             ten=parrot, five=egret, two=turtle, one=bird))
