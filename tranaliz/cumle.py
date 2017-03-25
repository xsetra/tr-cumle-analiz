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
            self.kelime_ekle(k, i)
            i += 1

    def cumle_bilgi_ver(self):
        temp = "Index : {} İçerik : {} {}".format(self.cumleIndex, self.cumleIcerik, self.kelimeleri_listele())
        return temp

    def kelime_ekle(self, kelime, index, tip=None):
        obj_kelime = Kelime()
        obj_kelime.kelimeIndex = index
        obj_kelime.kelimeIcerik = kelime
        obj_kelime.kelimeTipi = KelimeTipi(tip)
        self._cumleKelimeleri.append(obj_kelime)
        return obj_kelime

    def kelimeleri_listele(self):
        satirlar = "\n"
        for k in self._cumleKelimeleri:
            satirlar += '\t' + k.kelime_bilgi_ver()
        return satirlar

    def kelimeleri_sirala(self):
        sirali_liste = sorted(self._cumleKelimeleri, key=lambda sirala: sirala.kelimeIndex)
        self._cumleKelimeleri = sirali_liste
