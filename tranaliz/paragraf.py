# -*- coding: utf-8 -*-
from cumle import Cumle


class Paragraf:

    def __init__(self):
        self.paragrafIcerik = ""
        self._cumleler = []
        self.__last_cumle = 0

    def icerik_bol(self):
        cumle_list = self.paragrafIcerik.split('.')
        i = 1
        for c in cumle_list:
            self.cumle_ekle(i,c)
            i += 1

    def cumleleri_yaz(self):
        for c in self._cumleler:
            print(c.cumleIndex, c.cumleIcerik, c.kelimeleri_ver())

    def search_index(self, c_index):
        for c in self._cumleler:
            if c.cumleIndex == c_index:
                return c
        return None

    def cumle_ekle(self, index, icerik):
        objCumle = Cumle()
        objCumle.cumleIndex = index
        objCumle.cumleIcerik = icerik
        self._cumleler.append(objCumle)
        return objCumle

    @property
    def get_cumle(self):
        if self.__last_cumle == len(self._cumleler):
            self.__last_cumle = 0
        return_val = self._cumleler[self.__last_cumle]
        self.__last_cumle += 1
        return return_val
