from datetime import datetime, timedelta

class Covid:

    def __init__(self, date, cont, dia, total, obitos):
        
        # População do Brasil, fonte: IBGE 06/2020
        self.PouBR = float(221.8)

        self.Med = 0
        self.Date = date
        self.Dia = dia
        self.Total = total
        self.Obitos = obitos

        for i in range(0,9):
            self.Med += cont[i]
        self.Med /= 9

        pass

    def Print(self):
        
        #calculo e conversões
        self.TaxaLet = (self.Obitos/self.Total) * 100
        # taxaPOU = (self.Total / self.PouBR) * 100

        total = self.Total / 1000000
        obitos = self.Obitos / 1000
        registros = self.Dia / 1000
        media = self.Med /1000

        # formatação dos numeros
        # TxPou = '{:.2f}' .format(taxaPOU).replace('.',',')
        media = '{:.3f}' .format(media).replace('.',',')
        total = '{:.3f}' .format(total).replace('.',',')
        obitos = '{:.3f}' .format(obitos).replace('.',',')
        registros = '{:.3f}' .format(registros).replace('.',',')

        # SAIDA
        print("----------------------------------------------------------------------")
        print("\nTOTAL de CONTAMINAÇÕES: %s milhões de cont." % total)
        print("CONTAMINAÇÕES REGISTRADOS NO DIA:  %s mil cont." % registros)
        print("\nMÉDIA de CONTAMINAÇÕES: %s mil cont." % media)
        print("\nTOTAL de ÓBITOS: %s mil óbitos" % obitos)
        print("LETALIDADE: %.2f%%\n" % self.TaxaLet)
        print("----------------------------------------------------------------------")
        pass

    def Tabela(self, init, fim, intervalo):

        print("\nTABELA\n")

        for i in range (init, fim, intervalo):
    
            # CALCULO DA DATA
            delta = timedelta(days=i)
            dx = self.Date + delta
            s = dx.strftime("%d/%m/%y")
            print("DATA: %s" % s)

            # CALCULO DE CONTAMINAÇÕES
            dia = (self.Total + (self.Med * i)) / 1000000 + 0.001
            obitos = dia * (self.TaxaLet/100) * 1000000 + 1000
            obitos /= 1000
            dia = '{:.3f}' .format(dia).replace('.',',')
            obitos = '{:.3f}' .format(obitos).replace('.',',')
            
            print("CONT. %d dias: %s milhões cont." % (i, dia))
            print("N. de Óbitos: %s mil óbitos.\n" % obitos )

        pass



