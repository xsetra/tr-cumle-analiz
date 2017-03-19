# -*- coding: utf-8 -*-

from kelime import *

class Cumle:

    def __init__(self):
        self.cumleIndex = 0
        self.cumleIcerik = ""
        self._cumleKelimeleri = []

    def kelimelere_bol(self):
        self.cumleIcerik = self.cumleIcerik.strip()
        kelime_list = self.cumleIcerik.split(' ')
        i = 1
        for k in kelime_list:
            self.kelime_ekle(k,i)
            i += 1

    def kelime_ekle(self, kelime, index, tip=None):
        objKelime = Kelime()
        objKelime.kelimeIndex = index
        objKelime.kelimeIcerik = kelime
        objKelime.kelimeTipi = KelimeTipi(tip)
        self._cumleKelimeleri.append(objKelime)

    def kelimeleri_yaz(self):
        for k in self._cumleKelimeleri:
            print(k.kelimeIndex, k.kelimeIcerik)

    def kelimeleri_ver(self):
        satirlar = "\n"
        for k in self._cumleKelimeleri:
            satirlar += '\t' + str(k.kelimeIndex) + ' - ' + k.kelimeIcerik + ' - ' + str(k.kelimeTipi.name) + ' - ' + str(k.kelimeEk) + '\n'
        return satirlar
