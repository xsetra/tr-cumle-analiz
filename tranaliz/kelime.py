# -*- coding: utf-8 -*-
from enum import Enum


class KelimeTipi(Enum):
    isim = 1
    fiil = 2
    zarf = 3
    sifat = 4
    ozel_isim = 5
    baglac = 6


class Kelime:
    def __init__(self):
        self.kelimeIndex = 0
        self.kelimeIcerik = ""
        self.kelimeTipi = KelimeTipi
        self.kelimeEk = 0
        self.kelimeFreq = 0

    def kelime_bilgi_ver(self):
        return str(self.kelimeIndex) + ' - ' + self.kelimeIcerik + ' - ' + str(self.kelimeTipi.name) + ' - ' + \
               str(self.kelimeEk) + '\n'
