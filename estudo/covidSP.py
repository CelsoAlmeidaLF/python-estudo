# -*- coding: utf-8 -*-

from datetime import datetime, timedelta
d = datetime(2020, 11, 5)

med = 0
min = 0
max = 0

minOut = [ 863, 437, 684, 473 ]
maxOut = [ 6553, 5627, 5394, 4923, 4299, 3678, 6702, 5614, 5375, 4928 ]
medNov = [ 1020, 648, 749, 4755 ]

# HOJE REV.
obitos = float(39549)
total = float(1123299)

for i in range(0,4):
    min += minOut[i]
min /= 4

for i in range(0, 10):
    max += maxOut[i]
max /= 10

for i in range(0,4):
    med += medNov[i]
med /= 4

tx = (obitos/total) * 100
total /= 1000000
stotal = '{:.3f}' .format(total).replace('.',',')
total *= 1000000

medTTL = max
# medTTL = med

print("MEDIA MIN. d/ OUT: %.0f CONT. P/DIA." % min)
print("MEDIA MAX. d/ OUT: %.0f CONT. P/DIA." % max)
print("\nMEDIA D/ NOV: %.0f CONT. P/DIA." % med)

print("\nTOTAL de CONTAMINADOS: %s milhões cont." % stotal )
print("TOTAL de ÓBITOS: %.0f óbitos" % obitos )
print("\nLETALIDADE em SP: %.2f%%" % tx )

print("\n TABELA ESTASTISCOS do EST. de SP\n")

for i in range (15, 65, 5):

    # CALCULO DA DATA
    delta = timedelta(days=i)
    dx = d + delta
    s = dx.strftime("%d/%m/%y")
    print("DATA: %s" % s)

    # CALCULO DE CONTAMINAÇÕES
    dia = (total + (medTTL * i)) / 1000000 + 0.001
    obitos = dia * (tx/100) * 1000000 + 1000
    dia = '{:.3f}' .format(dia).replace('.',',')
    print("CONT. em %d dias: %s milhões cont." % (i, dia))
    print("N. de Óbitos: %.0f óbitos.\n" % obitos )
