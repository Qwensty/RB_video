import csv
from utils.csverror import InstantiateCSVError
import os
class Product:
    pay_rate = 1.0
    all = []

    def __init__(self, __name="", price=0.0, quantity=0):
        """ Инициализация экземпляра класса"""
        self.__name = __name
        self.price = price
        self.quantity = quantity
        self.all.append(self)
        if len(__name) > 10:
            raise NameError("Длина названия товара не должна превышать 10 символов!")

    @property
    def item_name(self):
        return self.__item_name

    @item_name.setter
    def item_name(self, value) -> str:
        if len(value) > 10:
            print("Exception: наименование товара превышает 10 символов")
        else:
            self.__item_name = value


    def __repr__(self) -> str:

        text = ""
        for dic in self.__dict__:
            text += dic + "=" + str(self.__dict__[dic]) + ", "
        return f"Product({text[:-2]})"

    def __str__(self):
        return f"Товар: {self.__name}, цена: {self.price}, количество: {self.quantity}"

    def calculate_amount(self):

        return self.price * self.quantity

    def apply_discount(self):

        self.price = self.price * self.pay_rate
        return self.price

    @classmethod
    def load_from_csv(cls, path) -> list:
        """
        Метод загружает данные из файла csv, путь к которому
        передан в параметре path и создает объекты класса Product
        в соответствии с данными из файла.
        """
        if os.path.exists(path) and os.path.isfile(path):
            with open(path, "r", newline='') as csvfile:
                csv_data = csv.DictReader(csvfile)
                if not (("name" in csv_data.fieldnames) and ("price" in csv_data.fieldnames) and ("quantity" in csv_data.fieldnames)):
                    raise InstantiateCSVError(f"Файл {path} поврежден")
                else:
                    Product_list = []
                    for row in csv_data:
                        name = row['name']
                        price = int(row['price']) if float(row['price']).is_integer \
                            else float(row['price'])
                        quantity = int(row['quantity']) if \
                            float(row['quantity']).is_integer\
                            else float(row['quantity'])
                        Product_list.append(cls(name, price, quantity))
                    return Product_list
        else:
            raise FileNotFoundError(f"Отсутствует файл {path}")

    @staticmethod
    def is_integer(number) -> bool:
        return ((type(number) == int) or (type(number) == float)) \
            and (round(number) == number)

class Phone(Product):
    def __init__(self, name="", price=0.0, quantity=0, number_of_sim=1):
        Product.__init__(self, name, price, quantity)
        self._number_of_sim = number_of_sim
        self.name = name
        if number_of_sim == 0:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")


    @staticmethod
    def add_item(data1, data2):
        if (isinstance(data1, Phone) or isinstance(data1, Product)) and \
            (isinstance(data2, Phone) or isinstance(data2, Product)):
            return data1.quantity + data2.quantity
        else:
            raise (ValueError, "Объекты должны быть типа Phone или Goods")

    def __repr__(self) -> str:
        text = "Phone("
        for dic in self.__dict__:
            text += f'{dic}={self.__dict__[dic]}, '
        return f"{text[:-2]})"

    def __str__(self) -> str:
        return f"Телефон: {self.name}, цена: {self.price}, \
количество: {self.quantity}, количество сим-карт: {self._number_of_sim}"

    @property
    def number_of_sim(self):
        return self._number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, number: int):
        if isinstance(number, int) and number > 0:
            self._number_of_sim = number
        else:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")