# -*- coding: utf-8 -*-
import pytest
from item import Item
from phone import Phone

class TestPhone:
    def setup_method(self):
        self.phone1 = Phone("Phone 1", 100, 2, 1)
        self.phone2 = Phone("Phone 2", 150, 3, 2)
        self.item = Item("Other Item", 50, 1)

    def test_make_call(self):
        assert self.phone1.make_call() == "Making a call with 1 SIM cards"
        assert self.phone2.make_call() == "Making a call with 2 SIM cards"

    def test_add_phones(self):
        result = self.phone1 + self.phone2
        assert result == 5

    def test_add_phone_with_item(self):
        with pytest.raises(TypeError):
            result = self.phone1 + self.item
