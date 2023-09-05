class Item:
    def __init__(self, name, price, quantity):
        """
        Конструктор класса Item.

        Args:
            name (str): Название товара.
            price (float): Цена товара.
            quantity (int): Количество товара.
        """
        self.name = name
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        """
        Возвращает строковое представление объекта Item, которое может быть использовано для восстановления объекта.

        Returns:
            str: Строковое представление объекта Item.
        """
        return f"Item('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        """
        Возвращает строковое представление объекта Item.

        Returns:
            str: Строковое представление объекта Item.
        """
        return self.name


if __name__ == '__main__':
    # Тестирование
    item1 = Item("Смартфон", 10000, 20)
    assert repr(item1) == "Item('Смартфон', 10000, 20)"
    assert str(item1) == 'Смартфон'
