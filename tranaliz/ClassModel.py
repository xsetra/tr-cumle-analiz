# -*- coding: utf-8 -*-


class ClassModel:
    def __init__(self):
        self.sinifAdi = None
        self.sinifNitelikleri = []
        self.sinifMetotlari = []

    def nitelik_ekle_listeden(self, liste_kelime):
        for k in liste_kelime:
            if k.kelimeIcerik != self.sinifAdi.kelimeIcerik:
                self.sinifNitelikleri.append(k)