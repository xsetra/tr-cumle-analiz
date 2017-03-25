# -*- coding: utf-8 -*-

from kelime import Kelime
from kelime import KelimeTipi
import copy


class Cumle:

    def __init__(self):
        self.cumleIndex = 0
        self.cumleIcerik = ""
        self._cumleKelimeleri = []
        self._isimTamlamalari = {}

    def kelimelere_bol(self):
        self.cumleIcerik = self.cumleIcerik.strip()
        kelime_list = self.cumleIcerik.split(' ')
        i = 1
        for k in kelime_list:
            self.kelime_ekle(k, i)
            i += 1

    def cumle_bilgi_ver(self):
        temp = "Index : {} - İçerik : {} {}".format(self.cumleIndex, self.cumleIcerik, self.kelimeleri_listele())
        return temp

    def kelime_ekle(self, kelime_icerik, index, tip=None):
        obj_kelime = Kelime()
        obj_kelime.kelimeIndex = index
        obj_kelime.kelimeIcerik = kelime_icerik
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

    def isim_tamlamalarini_bul(self):
        i = 0
        for k in self._cumleKelimeleri:
            kelime_list = []
            if i != 0:
                if k.kelimeTipi.name == 'isim' and last_kelime.kelimeTipi.name == 'isim':

                    kelime_list.append(k)
                    kelime_list.append(tmp_kelime)
                    Kelime.kelime_concat(k, last_kelime)
                    self._isimTamlamalari[last_kelime.kelimeIcerik] = kelime_list
            i += 1
            last_kelime = copy.copy(k)
            tmp_kelime = copy.copy(k)


