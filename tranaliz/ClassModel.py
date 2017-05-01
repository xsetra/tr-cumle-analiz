# -*- coding: utf-8 -*-


class ClassModel:
    def __init__(self):
        self.sinifAdi = None
        self.sinifNitelikleri = []
        self.sinifMetotlari = []
        self.cumleIndexes = []

    def nitelik_ekle_listeden(self, cumle_obj, ruleset_obj):
        for nitelik in cumle_obj._cumleIsimleri:
            if nitelik.kelimeIcerik == self.sinifAdi.cumleIcerik:
                continue
            else:
                for class_model in ruleset_obj._sinifAdaylari:
                    if nitelik.kelimeIcerik == class_model.sinifAdi.cumleIcerik: # 2 sınıf arasında, ilişki var
                        ruleset_obj._iliskiliSiniflar[nitelik.kelimeIcerik] = class_model.sinifAdi.cumleIcerik
                        break
            self.nitelik_ekle(nitelik)

    def nitelik_ekle(self, kelime_nitelik):
        if(self.nitelik_var_mi(kelime_nitelik)):
            return
        else:
            self.sinifNitelikleri.append(kelime_nitelik)

    def nitelik_var_mi(self, nitelik):
        for k in self.sinifNitelikleri:
            if k.kelimeIcerik == nitelik.kelimeIcerik:
                return True
        return False


    def nitelikleri_listele(self):
        tmp_str = "\nNitelikler\n"
        for n in self.sinifNitelikleri:
            tmp_str += "\t"+n.kelime_ayrintili_bilgi_ver()+"\n"
        return tmp_str
