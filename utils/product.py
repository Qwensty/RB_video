class Product():
    pay_rate=1.0
    def __init__(self, name="", price=0.0, quantity=0):
        self.name = name
        self.price = price
        #self.pay_rate = pay_rate
        #self.price_discount = price
        self.quantity = quantity

    def __repr__(self) -> str:
        text = ""
        for dic in self.__dict__:
            text += dic + "=" + str(self.__dict__[dic]) + ", "
        return text[:-2]

    def calculate_amount(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate