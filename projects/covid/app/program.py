# -*- coding: utf-8 -*-
import os
import sys
from app import *
from datetime import datetime
from .modules.covid.covid import Covid

class Program:
    """class Program"""
    def __init__(self):
        """contruct"""
        self.__init__
        pass
        
    def Program(self):
        """Method Init Program"""
        date = datetime.now()

        #DATA: 23/11/2020
        # BRASIL
        #reg_br = float(18615)
        #total_br = float(6071401)
        #obitos_br = float(169183)

        # SÃO PAULO
        reg_sp = float(4153)
        total_sp = float(1209588)
        obitos_sp = float(41267)


        # Dados ultimos dias BR.
        # cont_br = [23976, 11843, 8501, 10100, 18947, 22282, 26106, 26629, 29787 ]
        cont_sp = [ 4159,  5087, 9058,  6794,  6421,  8698,   737,  4640,  6130 ]

        self.GetCovid(date, cont_sp, reg_sp, total_sp, obitos_sp)
        pass

    def GetCovid(self, date, cont, reg, total, obitos):
        print("\nCOVID19 - SP")
        self.covid = Covid(date, cont, reg, total, obitos)
        self.covid.Print()
        self.covid.Tabela(15, 65, 5)
        pass

"""python script"""
if __name__ == "__main__":
    import sys
    prog = Program()
    prog.Program()