import pytest
from utils.product import Product


@pytest.fixture()
def mouse():
    mouse = Product("мышь Tech", 400, 5)
    return mouse

@pytest.fixture()
def keyboard():
    keyboard = Product("клавиатура Tech", 500, 0)
    return keyboard
