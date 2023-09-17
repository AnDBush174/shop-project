# test_instantiate.py
from src.item import Item
import os


def test_instantiate_from_csv():
    item = Item('name', 10.0, 5)  # �������� ���������� ������ Item
    item.instantiate_from_csv()
    # �������� ���������� ����� ��� ������������
    file_content = "name,price,quantity\nApple,1.0,5\nBanana,0.5,10"
    with open("test_items.csv", "w") as file:
        file.write(file_content)

    # �������� �������� �������� Item �� ����� CSV
    items = Item.instantiate_from_csv("src/items.csv")
    assert len(items) == 2
    assert items[0].name == "Apple"
    assert items[0].price == 1.0
    assert items[0].quantity == 5
    assert items[1].name == "Banana"
    assert items[1].price == 0.5
    assert items[1].quantity == 10

    # �������� ���������� �����
    os.remove("test_items.csv")
