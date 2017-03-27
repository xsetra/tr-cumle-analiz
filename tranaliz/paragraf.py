# -*- coding: utf-8 -*-
from cumle import Cumle


class Paragraf:

    def __init__(self):
        self.paragrafIcerik = ""
        self._cumleler = []
        self.__last_cumle = 0
        self._isimTamlamalari = []
        self._isimler = []
        self._fiiller = []
        self.__isimFreqToplam = 0
        self.__isimTamlamaFreqToplam = 0

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


