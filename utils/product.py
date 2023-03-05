import csv


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
        """ Метод возвращает представление класса. Выводит все атрибуты объекта"""
        text = ""
        for dic in self.__dict__:
            text += dic + "=" + str(self.__dict__[dic]) + ", "
        return f"Product({text[:-2]})"

    def __str__(self):
        return f"Товар: {self.__name}, цена: {self.price}, количество: {self.quantity}"

    def calculate_amount(self):
        """Метод возвращает общую стоимость всех товаров в экземпляре """
        return self.price * self.quantity

    def apply_discount(self):
        """Метод возвращает цену, рассчитанную с учетом уровня скидки pay_rate"""
        self.price = self.price * self.pay_rate
        return self.price

    @classmethod
    def load_from_csv(cls, path) -> list:

        with open(path, "r", newline='') as csvfile:
            csv_data = csv.DictReader(csvfile)
            goods_list = []
            for row in csv_data:
                goods_list.append(cls(row['name'], int(row['price']), int(row['quantity'])))
            return goods_list

    @staticmethod
    def is_integer(number) -> bool:
        """метод возвращает True- если переданное число number 
        имеет тип int, иначе - False"""
        return ((type(number) == int) or (type(number) == float)) \
            and (round(number) == number)
