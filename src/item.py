# item.py
import csv
import os
import chardet


def detect_encoding(file_path):
    with open(file_path, 'rb') as file:
        raw_data = file.read()
        result = chardet.detect(raw_data)
        return result['encoding']


class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def instantiate_from_csv(file_path):
        try:
            file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'src', 'items.csv')
            items = []  # список для хранения объектов Item
            encoding = detect_encoding(file_path)
            with open(file_path, 'r', encoding=encoding) as file:
                reader = csv.reader(file)
                is_header = True
                for row in reader:
                    if is_header:  # пропустить первую строку с заголовками столбцов
                        is_header = False
                        continue
                    if len(row) != 3:
                        raise InstantiateCSVError("Файл items.csv поврежден")
                    name = row[0]
                    price_str = row[1]
                    try:
                        price = float(price_str)
                    except ValueError:
                        raise InstantiateCSVError(f"Некорректное значение цены: {price_str}")
                    quantity = int(row[2])

                    item_exists = False
                    for item in items:
                        if item.name == name:
                            item_exists = True
                            item.quantity += quantity
                            break

                    if not item_exists:
                        item = Item(name, price, quantity)
                        items.append(item)  # добавляем объект item в список items
                    print(f"Добавлен товар: {item.name} ({item.quantity} шт.) по цене {item.price}")

        except FileNotFoundError:
            raise FileNotFoundError("Отсутствует файл items.csv") from None
        except csv.Error:
            raise InstantiateCSVError("Файл items.csv поврежден")


class InstantiateCSVError(Exception):
    pass


Item.instantiate_from_csv("src/items.csv")



