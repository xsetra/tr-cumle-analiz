# -*- coding: utf-8 -*-

from cumle import Cumle
from kelime import *
from ClassModel import ClassModel


class Ruleset:
    def __init__(self):
        self._sinifAdaylari = []
        self._siniflar = []

    def sinif_adayi_ekle(self, pkelime=None, icerik=None, freq=None, tip=None, ek=None, cumle_kelimeleri=None):
        sinif_model = ClassModel()
        c = Cumle()
        if pkelime is not None:
            c.cumleIcerik = pkelime.kelimeIcerik
            c._cumleKelimeleri.append(pkelime)

        if cumle_kelimeleri is not None:
            c.cumleIcerik = cumle_kelimeleri[1].kelimeIcerik + " "
            c.cumleIcerik += cumle_kelimeleri[0].kelimeIcerik
            c._cumleKelimeleri = cumle_kelimeleri

        sinif_model.sinifAdi = c
        self._sinifAdaylari.append(sinif_model)

    def sinif_adaylari_listele(self):
        str_tmp = "\n"
        for aday in self._sinifAdaylari:
            str_tmp += "\n >>> Sınıf Adayı ::: "
            str_tmp += str(aday.sinifAdi.cumle_bilgi_ruleset())
            str_tmp += "\n\tNitelikler :::"
            str_tmp += "\t\t" + aday.nitelikleri_listele()
        return str_tmp



