# -*- coding: utf-8 -*-
# src/phone.py
from item import Item


class Phone(Item):
    def __init__(self, name, price, quantity, number_of_sim):
        super().__init__(name, price, quantity)
        self.number_of_sim = number_of_sim

    def __add__(self, other):
        if isinstance(other, Phone):
            return self.quantity + other.quantity
        else:
            raise TypeError("Операция сложения недоступна для экземпляров класса Phone и других классов.")

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Phone('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"
