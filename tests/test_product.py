import pytest
import pytest_cov
from utils.product import Product


def test__init__(mouse):
    assert mouse._Goods__name == "мышь Tech"
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


def test__repr__(mouse):
    assert str(mouse) == "Goods(_Goods__name=мышь Tech, price=400, quantity=5)"