# -*- coding: utf-8 -*-

from kelime import Kelime
from kelime import KelimeTipi
from kelime import Noktalama
import copy


class Cumle:

    def __init__(self):
        self.cumleIndex = 0
        self.cumleIcerik = ""
        self.cumleLocation = 0
        self._cumleKelimeleri = []
        self._isimTamlamalari = []
        self._sifatTamlamalari = []
        self._cumleIsimleri = []
        self._cumleFiilleri = []

    def kelimelere_bol(self):
        self.cumleIcerik = self.cumleIcerik.strip()
        kelime_list = self.cumleIcerik.split(' ')
        i = 1
        for k in kelime_list:
            self.kelime_ekle(k, i)
            i += 1

    def cumle_bilgi_ver(self):
        temp = "Index : {} - İçerik : {} {}".format(self.cumleIndex, self.cumleIcerik, self.kelimeleri_listele())
        return temp

    def cumle_bilgi_ruleset(self):
        temp = "Index : {} - İçerik : {} {}".format(self.cumleIndex, self.cumleIcerik, self.kelimeleri_listele())
        return temp

    def kelime_ekle(self, kelime_icerik, index, tip=None, noktalama=None):
        obj_kelime = Kelime()
        obj_kelime.kelimeIndex = index
        obj_kelime.kelimeIcerik = kelime_icerik
        obj_kelime.kelimeTipi = KelimeTipi(tip)
        obj_kelime.kelimeNoktalama = Noktalama(noktalama)
        self._cumleKelimeleri.append(obj_kelime)
        return obj_kelime

    def kelimeleri_listele(self):
        satirlar = "\n"
        for k in self._cumleKelimeleri:
            satirlar += '\t' + k.kelime_bilgi_ver()
        return satirlar

    def kelimeleri_sirala(self):
        sirali_liste = sorted(self._cumleKelimeleri, key=lambda sirala: sirala.kelimeIndex)
        self._cumleKelimeleri = sirali_liste

    def cumle_isimlerini_duzenle(self):
        i = 0
        pop_list = []
        for isim in self._cumleIsimleri:
            if i != 0:
                if (isim.kelimeIndex - 1) == last_isim.kelimeIndex and last_isim.kelimeNoktalama.name == 'empty':
                    last_isim.kelimeIcerik += "_" + isim.kelimeIcerik
                    pop_list.append(i)
            i += 1
            last_isim = isim
        for willPop in pop_list:
            self._cumleIsimleri.pop(willPop)

    def isim_tamlamalarini_bul(self):
        pop_list = []
        i = 0
        for k in self._cumleKelimeleri:
            if i != 0:
                if k.kelimeTipi.name == 'isim' and last_kelime.kelimeTipi.name == 'isim' \
                        and last_kelime.kelimeNoktalama.name == 'empty':
                    pop_list.append(i)
                    last_kelime.kelimeIcerik += "_" + k.kelimeIcerik
                    self._cumleKelimeleri[i-1] = last_kelime
                    self._isimTamlamalari.append(last_kelime)
                    """tamlama = Cumle()
                    tamlama.cumleIndex = 1
                    Kelime.kelime_concat(k, last_kelime)
                    tamlama.cumleIcerik = last_kelime.kelimeIcerik

                    tamlama._cumleKelimeleri.append(k)
                    tamlama._cumleKelimeleri.append(tmp_kelime)
                    self._isimTamlamalari.append(tamlama)"""
            i += 1
            last_kelime = copy.copy(k)
        for willPop in pop_list:
            self._cumleKelimeleri.pop(willPop)

    def cumle_isimlerini_listele(self):
        tmp_str = "\nCÜMLE İSİMLERİ\n"
        for k in self._cumleIsimleri:
            tmp_str += '\t' + k.kelime_bilgi_ver()
        return tmp_str

    def cumle_fiillerini_listele(self):
        tmp_str = "\nCÜMLE FİİLLERİ\n"
        for k in self._cumleFiilleri:
            tmp_str += '\t' + k.kelime_bilgi_ver()
        return tmp_str

    def sifat_tamlamalarini_bul(self):


