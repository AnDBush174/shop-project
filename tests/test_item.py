import unittest
import csv
import os
from src.item import Item


class TestItem(unittest.TestCase):
    def setUp(self):
        Item.all = []

    def test_instantiate_from_csv(self):
        self.instantiate_from_csv()
        self.assertEqual(len(Item.all), 3)
        self.assertEqual(Item.all[0].name, "Item1")
        self.assertEqual(Item.all[0].price, 10.0)
        self.assertEqual(Item.all[0].quantity, 5)

    @staticmethod
    def instantiate_from_csv():
        with open("items.csv", mode='r') as file:
            reader = csv.DictReader(file)
            next(reader)  # Пропустить строку с заголовками
            for row in reader:
                item = Item(name=row['name'], price=float(row['price']), quantity=int(row['quantity']))
                Item.all.append(item)


    @classmethod
    def setUpClass(cls):
        cls.test_csv_path = "test_items.csv"
        cls.test_items = [
            {"name": "Item1", "price": "10.0", "quantity": "5"},
            {"name": "Item2", "price": "20.0", "quantity": "3"},
            {"name": "Item3", "price": "30.0", "quantity": "8"}
        ]
        with open(cls.test_csv_path, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["name", "price", "quantity"])
            writer.writeheader()
            writer.writerows(cls.test_items)

        Item.instantiate_from_csv()

    @classmethod
    def tearDownClass(cls):
        if os.path.exists(cls.test_csv_path) and os.path.getsize(cls.test_csv_path) > 0:
            os.remove(cls.test_csv_path)

    def setUp(self):
        Item.all.clear()

    def tearDown(self):
        Item.all.clear()

    class TestItem(unittest.TestCase):
        def setUp(self):
            Item.all = []

    # остальные тесты...


    def test_calculate_total_price(self):
        item = Item("Test Item", 10.0, 2)
        self.assertEqual(item.calculate_total_price(), 20.0)

    def test_apply_discount(self):
        item = Item("Test Item", 10.0, 1)
        item.apply_discount()
        self.assertEqual(item.price, 10.0)

    def test_string_to_number(self):
        self.assertEqual(Item.string_to_number("10.0"), 10)
        self.assertEqual(Item.string_to_number("20.5"), 20)
        self.assertEqual(Item.string_to_number("30.7"), 30)


if __name__ == "__main__":
    unittest.main()
