#coding: utf-8

year = int(input("Digite o ano: "))

if year % 4 != 0:
    print("O ano {}, não é bissexto".format(year))
elif year % 100 != 0:
    print("O ano {}, é bissexto".format(year))
elif year % 400 != 0:
    print("O ano {}, não é bissexto".format(year))
else:
    print("O ano {}, é bissexto".format(year))
