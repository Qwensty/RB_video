import pytest
from utils.product import Product


def test__init__(mouse):
    assert mouse._Product__name == "мышь Tech"
    assert mouse.price == 400
    assert mouse.quantity == 5
    with pytest.raises(NameError, match="Длина названия товара не должна превышать 10 символов!"):
        item = Product("очень длинное имя", 1, 1 )


def test_calculate_amount(mouse, keyboard):
    assert mouse.calculate_amount() == 2000
    item1 = Product("name", 50, 2)
    assert item1.calculate_amount() == 100
    assert keyboard.calculate_amount() == 0


def test_apply_discount(mouse):
    assert mouse.pay_rate == 1
    item1 = Product("name", 50, 2)
    item1.pay_rate = 0.8
    assert item1.apply_discount() == 40
    assert item1.price == 40
    assert int(item1.calculate_amount()) == 80


#def test__repr__(mouse):
 #   assert str(mouse) == "Product(_Product__name=мышь Tech, price=400, quantity=5)"


def test_is_integer():
    item = Product("name", 50, 2)
    assert item.is_integer(5) is True
    assert item.is_integer(5.0) is True
    assert item.is_integer(5.5) is False
    assert item.is_integer("5") is False


def test_load_from_csv(patf_csv_file) -> list:
    item = Product("name", 50, 2)
    assert len(item.load_from_csv(patf_csv_file)) == 5
    assert isinstance(item.load_from_csv(patf_csv_file)[0], Product)

def test__str__():
    assert str(Product("Ноутбук", 20000, 5)) == "Товар: Ноутбук, цена: 20000, количество: 5"
    assert str(Product("Смартфон", 100, 1)) == "Товар: Смартфон, цена: 100, количество: 1"
