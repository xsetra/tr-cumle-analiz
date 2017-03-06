# -*- coding: utf-8 -*-

from kelime import *

class Cumle:
    
    def __init__(self):
        self.cumleIndex = 0
        self.cumleIcerik = ""
        self.cumleKelimeleri = []

    def kelimelere_bol(self):
        self.cumleIcerik = self.cumleIcerik.strip()
        kelime_list = self.cumleIcerik.split(' ')
        i = 1
        for k in kelime_list:
            objKelime = Kelime()
            objKelime.kelimeIndex = i
            objKelime.kelimeIcerik = k
            
            # Burada veritabanı bağlantısı yapıp, kelimeIceriğinin tipini
            #ögrenecegiz.
            # TODO

            self.cumleKelimeleri.append(objKelime)
            i += 1

    def kelimeleri_yaz(self):
        for k in self.cumleKelimeleri:
            print(k.kelimeIndex, k.kelimeIcerik)
