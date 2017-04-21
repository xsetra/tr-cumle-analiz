# -*- coding: utf-8 -*-
from enum import Enum


class KelimeTipi(Enum):
    isim = 1
    fiil = 2
    zarf = 3
    sifat = 4
    ozel_isim = 5
    baglac = 6


class Noktalama(Enum):
    empty = 0
    virgul = 1
    noktali_virgul = 2


class Kelime:
    def __init__(self):
        self.kelimeIndex = 0
        self.kelimeIcerik = ""
        self.kelimeTipi = KelimeTipi
        self.kelimeEk = 0
        self.kelimeFreq = 0
        self.kelimeNoktalama = Noktalama

    def kelime_bilgi_ver(self):
        return str(self.kelimeIndex) + ' - ' + self.kelimeIcerik + ' - ' + str(self.kelimeTipi.name) + ' - ' + str(self.kelimeEk)

    def kelime_ayrintili_bilgi_ver(self):
        return str(self.kelimeIndex) + ' - ' + self.kelimeIcerik + ' - ' + str(self.kelimeTipi.name) + ' - ' + str(self.kelimeEk) + ' - ' + str(self.kelimeFreq)

    @staticmethod
    def kelime_concat(kaynak, hedef):
        hedef.kelimeIcerik += " " + kaynak.kelimeIcerik
        hedef.kelimeEk += kaynak.kelimeEk
        hedef.kelimeEk %= 2
