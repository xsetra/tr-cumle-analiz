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
