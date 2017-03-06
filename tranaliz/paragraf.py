# -*- coding: utf-8 -*-
from cumle import Cumle

class Paragraf:
   
    def __init__(self):
        self.paragrafIcerik = ""
        self.cumleler = []
        
    def icerik_bol(self):
        cumle_list = self.paragrafIcerik.split('.')
        i = 1        
        for c in cumle_list:
            objCumle = Cumle()
            objCumle.cumleIndex = i
            objCumle.cumleIcerik = c
            objCumle.kelimelere_bol()
            self.cumleler.append(objCumle)
            i += 1

    def cumleleri_yaz(self):
        for c in self.cumleler:
            print(c.cumleIndex, c.cumleIcerik)


            
