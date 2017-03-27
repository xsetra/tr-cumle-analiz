#! /usr/bin/env python3
# -*- coding: utf-8 -*-


from kelime import Kelime
from kelime import KelimeTipi
from cumle import Cumle
from paragraf import Paragraf
from mysql import Veritabani
from ruleset import Ruleset
from ClassModel import ClassModel

dokuman = Paragraf()
db = Veritabani()
kurallar = Ruleset()

db.baglan()
db.kelime_bilgi(dokuman)

dokuman.isim_tamlamalarini_topla()
print(dokuman.isim_tamlamalarini_listele())

db.isim_ve_fiil_cek(dokuman)

print("--İsimler--")
print(dokuman.isimleri_listele())
print("--Fiiller--")
print(dokuman.fiilleri_listele())


"""print (dokuman._cumleler[0].cumle_isimlerini_listele())
print (dokuman._cumleler[0].cumle_fiillerini_listele())"""


dokuman.isim_sinif_adayi(kurallar)
dokuman.isim_tamlama_sinif_adayi(kurallar)


dokuman.search_cumle_fiilleri(kurallar)

print(kurallar.sinif_adaylari_listele())

db.kapat()
