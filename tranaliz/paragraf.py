# -*- coding: utf-8 -*-
from cumle import Cumle
from kelime import *


class Paragraf:
    __specialVerbs = ["içermek","sahip olmak","dahil olmak","yer almak","bulundurmak","olmak","bulunmak"]
    kelimeSayisi = 0

    def __init__(self):
        self.paragrafIcerik = ""
        self._cumleler = []
        self.__last_cumle = 0
        self._isimTamlamalari = []
        self._isimler = []
        self._fiiller = []
        self.__isimFreqToplam = 0
        self.__isimTamlamaFreqToplam = 0
        self._cumleSpecialVerbs = []

    def icerik_bol(self):
        cumle_list = self.paragrafIcerik.split('.')
        i = 1
        for c in cumle_list:
            cumle = Cumle()
            cumle.cumleIndex = i
            cumle.cumleIcerik = c
            self.cumle_ekle(cumle)
            i += 1

    def cumleleri_listele(self):
        for c in self._cumleler:
            print(c.cumle_bilgi_ver())

    def search_index(self, c_index):
        for c in self._cumleler:
            if c.cumleIndex == c_index:
                return c
        return None

    def cumle_ekle(self, index, icerik):
        obj_cumle = Cumle()
        obj_cumle.cumleIndex = index
        obj_cumle.cumleIcerik = icerik
        self._cumleler.append(obj_cumle)
        return obj_cumle

    def isim_tamlamalarini_topla(self):
        c = self.get_cumle()
        ekle = 1
        while c is not None:
            c.isim_tamlamalarini_bul()
            if len(c._isimTamlamalari) != 0:
                for t in c._isimTamlamalari:
                    if len(self._isimTamlamalari) == 0:
                        self._isimTamlamalari.append(t)
                        ekle = 0
                    else:
                        ekle = 1
                        for i in self._isimTamlamalari:
                            if t.cumleIcerik == i.cumleIcerik:
                                i.cumleIndex += 1
                                ekle = 0
                                break
                    if ekle == 1:
                        self._isimTamlamalari.append(t)
            c = self.get_cumle()

    def isim_tamlamalarini_listele(self):
        tmp_str = "\n"
        for t in self._isimTamlamalari:
            tmp_str += t.cumle_bilgi_ver() + "\n"
        return tmp_str

    def isimleri_listele(self):
        tmp_str = "\n"
        for i in self._isimler:
            tmp_str += i.kelime_ayrintili_bilgi_ver() + "\n"
        return tmp_str

    def fiilleri_listele(self):
        tmp_str = "\n"
        for i in self._fiiller:
            tmp_str += i.kelime_ayrintili_bilgi_ver() + "\n"
        return tmp_str

    def get_cumle(self):
        if self.__last_cumle == len(self._cumleler):
            self.__last_cumle = 0
            return None
        return_val = self._cumleler[self.__last_cumle]
        self.__last_cumle += 1
        return return_val

    def sum_isim_frekans(self):
        for isim in self._isimler:
            self.__isimFreqToplam += isim.kelimeFreq
        return self.__isimFreqToplam

    def isim_sinif_adayi(self, ruleset):
        self.sum_isim_frekans()
        for isim in self._isimler:
            if Paragraf.limit_calculate(freq=self.__isimFreqToplam, number=isim.kelimeFreq):
                ruleset.sinif_adayi_ekle(pkelime=isim)

    def sum_isim_tamlama_frekans(self):
        for cumle in self._isimTamlamalari:
            self.__isimTamlamaFreqToplam += cumle.cumleIndex

    @staticmethod
    def limit_calculate(freq, number):
        limit = 100 / freq
        limit = limit * number
        if limit >= 20:
            return 1
        else:
            return 0

    def isim_tamlama_sinif_adayi(self, ruleset):
        self.sum_isim_tamlama_frekans()
        for cumle in self._isimTamlamalari:
            if Paragraf.limit_calculate(self.__isimTamlamaFreqToplam, cumle.cumleIndex):
                ruleset.sinif_adayi_ekle(icerik=cumle.cumleIcerik,
                                         ek=-1,
                                         tip=KelimeTipi.isim,
                                         freq=cumle.cumleIndex)



    def _search_cumle_fiilleri(self, ruleset):
        for c in self._cumleler:
            breaking = 0
            for special in Paragraf.__specialVerbs:
                for fiil in c._cumleFiilleri:
                    if special == fiil.kelimeIcerik:
                        breaking = 1
                        break
                if breaking == 1:
                    break

            if breaking == 1:
                for isim in c._cumleIsimleri:
                    for aday in ruleset._sinifAdaylari:
                        if isim.kelimeIcerik == aday.sinifAdi.kelimeIcerik:
                            breaking = 2
                            break
                    if breaking == 2:
                        break
            if breaking == 2:
                aday.nitelik_ekle_listeden(c._cumleIsimleri)


