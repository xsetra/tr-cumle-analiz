# -*- coding: utf-8 -*-

from cumle import Cumle
from kelime import *


class Ruleset:

    def __init__(self):
        self.isimTamlamalari = []
        self._cumle = []

    @property
    def cumle(self):
        return self._cumle

    @cumle.setter
    def cumle(self, new_val):
        self._cumle.append(new_val)

    @staticmethod
    def kelime_concat(kaynak, hedef):
        hedef.kelimeIcerik += " "+kaynak.kelimeIcerik
        hedef.kelimeEk += kaynak.kelimeEk
        hedef.kelimeEk %= 2

    def cumle_kelimelerini_sirala(self):
        for c in self._cumle:
            c.kelimeleri_sirala()

    def isim_tamlamasi_bul(self):
        combo = 0
        last_kelime = Kelime()
        sonEleman = Kelime()
        i = 0
        for k in self._cumle._cumleKelimeleri:
            if i != 0:
                if k.kelimeTipi == KelimeTipi.baglac:
                    continue
                if last_kelime.kelimeTipi == KelimeTipi.isim and k.kelimeTipi == KelimeTipi.isim:
                    combo += 1
                    if combo <= 1:
                        Ruleset.kelime_concat(k, last_kelime)
                        last_kelime.kelimeFreq += 1
                        self.isimTamlamalari.append(last_kelime)

                    else:
                        sonEleman = self.isimTamlamalari.pop()
                        Ruleset.kelime_concat(k, sonEleman)
                        sonEleman.kelimeFreq += 1
                        self.isimTamlamalari.append(sonEleman)
                else:
                    combo = 0

            i += 1
            last_kelime = k

    def isim_tamlamalari_listele(self):
        for t in self.isimTamlamalari:
            print(t.kelimeFreq, t.kelime_bilgi_ver())
