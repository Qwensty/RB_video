from utils.product import Product, Phone
from data.config import path_csv
from utils.keyboard import KeyBoard
from utils.csverror import InstantiateCSVError

def main():
    # Задание 6
    # Файл items.csv отсутствует
    item = Product("Ноутбук", 20000, 5)
    try:
        print(repr(item.load_from_csv(path_csv)))
    except FileNotFoundError as error:
        print(error)
       # В файле items.csv удалена последняя колонка.
    try:
        item.load_from_csv(r'data\items.csv')
    except InstantiateCSVError as error:
        print(error)
        # InstantiateCSVError: Файл item.csv поврежден


if __name__ == "__main__":
    main()

