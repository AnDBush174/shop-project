# -*- coding: utf-8 -*-
# src/item.py
class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"

    def increase_quantity(self, increment):
        self.quantity += increment

    def decrease_quantity(self, decrement):
        self.quantity -= decrement

    def calculate_total_price(self):
        return self.price * self.quantity

    def __add__(self, other):
        if isinstance(other, Item):
            return self.quantity + other.quantity

        raise TypeError("Нельзя складывать Item с экземпляром другого класса")
