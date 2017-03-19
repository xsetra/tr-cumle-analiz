# -*- coding: utf-8 -*-

from cumle import Cumle
from kelime import *


class Ruleset:

    def __init__(self):
        self.isimTamlamalari = {}
        self._cumle = None

    @property
    def cumle(self):
        return self._cumle

    @cumle.setter
    def cumle(self, new_val):
        self._cumle = new_val

    def isim_tamlamasi_bul(self):
        
