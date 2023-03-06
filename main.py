from utils.product import Product, Phone
from data.config import path_csv


def main():
  #  try:
 #       item1 = Product("Смартфон_123456789", 10000, 20)
 #       print(item1.calculate_amount())
 #   except NameError:
 #       print("Ошибка. Длина названия товара не должна превышать 10 символов.")
#
 #   item2 = Product("Ноутбук", 20000, 5)
#
 #   print(item2.calculate_amount())
 #   Product.pay_rate = 0.8
#
 #   try:#
 #       print(item2.load_from_csv(path_csv))
 #   except FileNotFoundError:
 #       print(f"\nФайл {path_csv} не найден\n")
#
 #       print(item2.price)
 #       print(Product.all)
 #   item2.__name = "СуперСмартфон"


  phone1 = Phone("iPhone 14", 120_000, 5, 1)
  print(phone1)
  print(repr(phone1))

  print(phone1.number_of_sim)

  try:
      phone1.number_of_sim = 0
  except Exception as text:
      print(text)

  try:
      phone3 = Phone("gPhone 2", 5_000, 5, 0)
  except Exception as text:
      print(text)

  phone2 = Phone("mPhone 22", 30_000, 2, 1)
  print(phone1.add_item(phone1, phone2))


if __name__ == "__main__":
    main()
