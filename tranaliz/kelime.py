# -*- coding: utf-8 -*-
from enum import Enum

class KelimeTipi(Enum):
    isim = 1
    fiil = 2

class Kelime:
    def __init__(self):
        self.kelimeIndex = 0
        self.kelimeIcerik = ""
        self.kelimeTipi = None

