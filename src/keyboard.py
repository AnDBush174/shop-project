# src.py
# -*- coding: utf-8 -*-
from src.item import Item


class Keyboard(Item):
    def __init__(self, name, price, quantity, language):
        super().__init__(name, price, quantity)
        self._language = language

    @property
    def language(self):
        return self._language

    def change_lang(self):
        if self.language == 'EN':
            self._language = 'RU'
        else:
            self._language = 'EN'

    def __str__(self):
        return self.name
