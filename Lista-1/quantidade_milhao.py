#coding: utf-8

tam = 0

num = 2**1000000

for i in str(num):
    tam+=1

print("A quantidade de digitos que existe em 2^1000000 é de {}".format(tam))
