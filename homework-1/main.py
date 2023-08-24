class Item:
    """Класс для товара"""

    pay_rate = 1  # Уровень цен по умолчанию
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """Экземпляр инициализируется названием, ценой и количеством товара."""
        self.name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    def calculate_total_price(self) -> float:
        """Рассчитывает общую стоимость товара."""
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """Применяет скидку к цене товара с учетом уровня цен."""
        self.price *= self.pay_rate

    def __str__(self) -> str:
        """Возвращает строковое представление товара."""
        return f"Товар: {self.name}, Цена: {self.price}, Количество: {self.quantity}"


if __name__ == '__main__':
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)

    print(f"Общая стоимость товара {item1.name}: {item1.calculate_total_price()}")
    print(f"Общая стоимость товара {item2.name}: {item2.calculate_total_price()}")

    Item.pay_rate = 0.80
    print(f"Стоимость единицы товара {item1.name} без скидки: {item1.price}")
    item1.apply_discount()

    print(f"Стоимость единицы товара {item1.name} с учетом скидки: {item1.price}")
    print(f"Стоимость единицы товара {item2.name} без скидки: {item2.price}")

    print(f"Все товары: {Item.all}")
