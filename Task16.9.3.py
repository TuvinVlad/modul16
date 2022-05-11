class Client:
    def __init__(self, name, last_name, city, balance):
        self.name = name
        self.last_name = last_name
        self.city = city
        self.balance = balance

    def __str__(self):
        return f'{self.name}{self.last_name}. {self.city}. Баланс: {self.balance} руб.'


cl1 = Client('Иван ', 'Петров', 'Москва', 50)

print(cl1)
