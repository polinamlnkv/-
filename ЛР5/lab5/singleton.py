class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.value = None  # пример свойства
        return cls._instance

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value