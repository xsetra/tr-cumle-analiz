# -*- coding: utf-8 -*-

from cumle import Cumle
from kelime import *
from ClassModel import ClassModel


class Ruleset:
    def __init__(self):
        self._sinifAdaylari = []
        self._siniflar = []

    def sinif_adayi_ekle(self, pkelime=None, icerik=None, freq=None, tip=None, ek=None):
        sinif_model = ClassModel()
        if type(pkelime).__name__ != 'Kelime':
            pkelime = Kelime()
            pkelime.kelimeIcerik = icerik
            pkelime.kelimeFreq = freq
            pkelime.kelimeTipi = KelimeTipi(tip)
            pkelime.kelimeEk = ek
        sinif_model.sinifAdi = pkelime
        self._sinifAdaylari.append(sinif_model)

    def sinif_adaylari_listele(self):
        str_tmp = "\n"
        for aday in self._sinifAdaylari:
            str_tmp += aday.sinifAdi.kelime_ayrintili_bilgi_ver()+" \n>>> "+aday.nitelikleri_listele()+"\n"
        return str_tmp



