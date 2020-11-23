# -*- coding: utf-8 -*-

from datetime import datetime, timedelta
d = datetime(2020, 11, 5)

med = 0

cont = [23976, 11843, 8501, 10100, 18947, 22282, 26106, 26629, 29787]

for i in range(0,9):
    med += cont[i]
med /= 9

regD = float(23976)
total = float(5590025)
obitos = float(161106)
pouBR = float(221.8)

taxa = (obitos/total) * 100
total /= 1000000
taxaPOU = (total / pouBR) * 100

sTxPou = '{:.2f}' .format(taxaPOU).replace('.',',')
stotal = '{:.3f}' .format(total).replace('.',',')
sPOU = '{:.3f}' .format(pouBR).replace('.',',')
total *= 1000000

print("TOTAL de CONTAMINAÇÕES em TODO BRASIL: %s milhões de cont. " % stotal)

print("\nN. de Hab. no Brasil: %s hab. fonte: IBGE 06/2020" % sPOU)
print("%s%% da população brasileria já se contaminaram pelo coronavirus \n" % sTxPou)

print("TOTAL de ÓBITOS em TODO BRASIL: %.0f óbitos \n" % obitos)
print("LETALIDADE: %.2f%%\n" % taxa)
print("CONTAMINAÇÕES REGISTRADOS NO DIA:  %.0f" % regD)
print("MEDIA de CONTAMINADOS P/ DIA: %.0f" % med)

medTTL = med
# medTTL = regD

print("\nTABELA ESTASTISCOS\n")

for i in range (15, 105, 5):

    # CALCULO DA DATA
    delta = timedelta(days=i)
    dx = d + delta
    s = dx.strftime("%d/%m/%y")
    print("DATA: %s" % s)

    # CALCULO DE CONTAMINAÇÕES
    dia = (total + (medTTL * i)) / 1000000 + 0.001
    txmax = (dia / pouBR) * 100
    obitos = dia * (taxa/100) * 1000000 + 1000
    dia = '{:.3f}' .format(dia).replace('.',',')
    print("CONT. %d dias: %s milhões cont." % (i, dia))
    print("N. de Óbitos: %.0f óbitos.\n" % obitos )

    if(i >= 100 ):
        print("*Obs.: Até aqui serão: %.2f%% cont. da pou. no Brasil" % txmax)
