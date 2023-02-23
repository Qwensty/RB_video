from utils.product import Product


def main():
    item1 = Product("Смартфон", 10000, 20)
    item2 = Product("Ноутбук", 20000, 5)
    print(item1.calculate_amount())
    print(item2.calculate_amount())
    Product.pay_rate = 0.8

    item1.apply_discount()

    print(item1.price)
    print(item2.price)


if __name__ == "__main__":
    main()

