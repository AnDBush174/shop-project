import pytest
from src.keyboard import Keyboard


@pytest.fixture
def keyboard():
    return Keyboard('Dark Project KD87A', 9600, 5, 'EN')


def test_keyboard_initial_values(keyboard):
    assert keyboard.name == 'Dark Project KD87A'
    assert keyboard.price == 9600
    assert keyboard.quantity == 5
    assert keyboard.language == 'EN'


def test_keyboard_change_lang(keyboard):
    keyboard.change_lang()
    assert keyboard.language == 'RU'

    keyboard.change_lang()
    assert keyboard.language == 'EN'


def test_keyboard_str_representation(keyboard):
    assert str(keyboard) == 'Dark Project KD87A'


def test_keyboard_set_name(keyboard):
    assert keyboard.name == 'Dark Project KD87A'

    keyboard.name = 'New Keyboard Name'
    assert keyboard.name == 'New Keyboard Name'


def test_keyboard_price_quantity(keyboard):
    assert keyboard.price == 9600
    assert keyboard.quantity == 5

    keyboard.price = 8000
    keyboard.quantity = 10
    assert keyboard.price == 8000
    assert keyboard.quantity == 10


@pytest.mark.parametrize("name, price, quantity, language, expected", [
    ("Keyboard 1", 5000, 3, "RU", "Keyboard 1"),
    ("Keyboard 2", 10000, 0, "EN", "Keyboard 2"),
    ("Keyboard 3", 0, 10, "RU", "Keyboard 3"),
])
def test_keyboard_name_str_representation(name, price, quantity, language, expected):
    keyboard = Keyboard(name, price, quantity, language)
    assert str(keyboard) == expected
