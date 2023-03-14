from utils.product import Product


class Mixin():
    """
    Класс Mixin для реализации атрибута __language
    и метода change_language для смены его значения.
    """
    def __init__(self, language="EN") -> None:

        self._language = language

    def change_lang(self) -> str:
        """Метод меняет раскладку клавиатур EN на RU
        и наоборот. Возвращает текущее значение раскладки."""
        if self._language == "EN":
            self._language = "RU"
            return self._language
        elif self._language == "RU":
            self._language = "EN"
            return self._language

    @property
    def language(self) -> str:

        return self._language


class KeyBoard(Product, Mixin):
    """
    Класс KeyBoard- наследник класса Goods и миксина Mixin.
    """
    def __init__(self, name="", price=0.0, quantity=0, language="EN") -> None:

        super().__init__("", price, quantity)
        self._language = language
        self.name = name

    @property
    def name(self) -> str:

        return self.__name


    @name.setter
    def name(self, name: str) -> None:

        self.__name = name
        return self.name

    def __repr__(self) -> str:
        """ Метод возвращает представление класса.
        Выводит все атрибуты объекта"""
        text = "KeyBoard("
        for dic in self.__dict__:
            text += f'{dic}={self.__dict__[dic]}, '
        return f"{text[:-2]})"

    def __str__(self) -> str:
        """ Метод возвращает текст для печати, содержащий значения
        аттрибутов объектов класса KeyBoard"""
        return f"Клавиатура: {self.name}, цена: {self.price}, " + \
            f"количество: {self.quantity}"