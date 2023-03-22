class InstantiateCSVError(Exception):
    """
    Класс InstantiateCSVError для обработки исключения, возникающего
    при открытии csv-файла в случае, если в нем отсутствуют какие-либо
    необходимые столбцы.
    """
    def __init__(self, message=""):
        if message:
            self.message = message
        else:
            self.message = None

    def __str__(self):
        """Возвращает тип ошибки и сообщение"""
        return "InstantiateCSVError: " + str(self.message)