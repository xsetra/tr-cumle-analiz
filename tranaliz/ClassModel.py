# -*- coding: utf-8 -*-


class ClassModel:
    __specialMetotIsimleri = ["davranış", "metot"]

    def __init__(self):
        self.sinifAdi = None
        self.sinifNitelikleri = []
        self.sinifMetotlari = []
        self.cumleIndexes = []
        self.iliskiliSiniflar = []

    def metot_ekle(self, cumle_obj):
        for fiil in cumle_obj._cumleFiilleri:
            if self.metot_var_mi(fiil) is False:
                self.sinifMetotlari.append(fiil)

    def metot_var_mi(self, metot_kelime):
        if metot_kelime.kelimeIcerik in self.sinifMetotlari:
            return True
        return False

    def metotlari_listele(self):


    def nitelik_ekle_listeden(self, cumle_obj, ruleset_obj):
        for nitelik in cumle_obj._cumleIsimleri:
            if nitelik.kelimeIcerik == self.sinifAdi.cumleIcerik:
                continue
            else:
                for class_model in ruleset_obj._sinifAdaylari:
                    if nitelik.kelimeIcerik == class_model.sinifAdi.cumleIcerik: # 2 sınıf arasında, ilişki var
                        self.iliski_ekle(nitelik, cumle_obj)
                        break
            if self.nitelik_ekle(nitelik) == "metot":
                self.metot_ekle(cumle_obj)

    def iliski_listele(self):
        str_tmp = ""
        for iliski in self.iliskiliSiniflar:
            str_tmp += "\t" + iliski.kelimeIcerik + " : " + iliski.kelimeIliski + "\n"
        return str_tmp

    def iliski_ekle(self, nitelik_class, cumle_obj):
        i = 0
        length = len(cumle_obj._cumleKelimeleri)

        for k in cumle_obj._cumleKelimeleri:
            if k.kelimeIcerik == nitelik_class.kelimeIcerik:
                if (i+1) == length:
                    break
                elif cumle_obj._cumleKelimeleri[i+1].kelimeTipi.name == 'fiil':
                    nitelik_class.kelimeIliski = cumle_obj._cumleKelimeleri[i+1].kelimeIcerik
                    if self.iliski_var_mi(nitelik_class) is False:
                        self.iliskiliSiniflar.append(nitelik_class)
            i += 1

    def iliski_var_mi(self, iliski_kelime):
        for iliski in self.iliskiliSiniflar:
            if iliski.kelimeIcerik == iliski_kelime.kelimeIcerik:
                return True
        return False

    def nitelik_ekle(self, kelime_nitelik):
        if kelime_nitelik.kelimeIcerik in ClassModel.__specialMetotIsimleri:
            return "metot"
        if self.nitelik_var_mi(kelime_nitelik):
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
