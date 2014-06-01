#coding: utf-8

gain = float(input("Quanto você ganha por hora em R$: "))
hours = float(input("Quantas horas trabalhou no mês: "))

print("  O salario bruto no mês foi de R${bruto}\n  Pagou R${inss} para o INSS\n  Pagou R${sind} ao sindicato\n"
    "  O seu salario liquido foi de R${liquido}".format(bruto=gain*hours, inss=gain*hours*0.08, sind=gain*hours*0.05,
    liquido=gain*hours - gain*hours*0.08 - gain*hours*0.05 - gain*hours*0.11))
