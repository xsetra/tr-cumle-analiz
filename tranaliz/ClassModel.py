# -*- coding: utf-8 -*-


class ClassModel:
    def __init__(self):
        self.sinifAdi = None
        self.sinifNitelikleri = []
        self.sinifMetotlari = []
        self.cumleIndexes = []

    def nitelik_ekle_listeden(self, liste_kelime, sinif_adaylari):
        kelimeler = []
        for adaylar in sinif_adaylari:
            for kelime in sinif_adaylari._cumleKelimeleri:
                kelimeler.append(kelime)

        for k in liste_kelime:
            if k.kelimeIcerik != self.sinifAdi.cumleIcerik:
                for kelime in sinif_adaylari._cumleKelimeleri:
                    if k.kelimeIcerik != kelime.kelimeIcerik:
                        self.sinifNitelikleri.append(k)

    def nitelikleri_listele(self):
        tmp_str = "\nNitelikler\n"
        for n in self.sinifNitelikleri:
            tmp_str += "\t"+n.kelime_ayrintili_bilgi_ver()+"\n"
        return tmp_str
