# -*- coding: utf-8 -*-

from cumle import Cumle
from kelime import *


class Ruleset:
    def __init__(self):
        self._sinifAdaylari = []
        self._siniflar = []

    def sinif_adayi_ekle(self, pkelime=None, icerik=None, freq=None, tip=None, ek=None):
        if type(pkelime).__name__ != 'Kelime':
            pkelime = Kelime()
            pkelime.kelimeIcerik = icerik
            pkelime.kelimeFreq = freq
            pkelime.kelimeTipi = KelimeTipi(tip)
            pkelime.kelimeEk = ek
        self._sinifAdaylari.append(pkelime)




