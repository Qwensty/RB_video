from utils.product import Product
from data.config import path_csv


def main():
    try:
        item1 = Product("Смартфон_123456789", 10000, 20)
        print(item1.calculate_amount())
    except NameError:
        print("Ошибка. Длина названия товара не должна превышать 10 символов.")

    item2 = Product("Ноутбук", 20000, 5)

    print(item2.calculate_amount())
    Product.pay_rate = 0.8

    try:
        print(item2.load_from_csv(path_csv))
    except FileNotFoundError:
        print(f"\nФайл {path_csv} не найден\n")

        print(item2.price)
        print(Product.all)
    item2.__name = "СуперСмартфон"


if __name__ == "__main__":
    main()
