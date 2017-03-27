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

    def nitelikleri_listele(self):
        tmp_str = "\nNitelikler\n"
        for n in self.sinifNitelikleri:
            tmp_str += "\t"+n.kelime_ayrintili_bilgi_ver()+"\n"
        return tmp_str
