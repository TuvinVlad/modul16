class Client:
    def __init__(self, name, last_name, city, balance):
        self.name = name
        self.last_name = last_name
        self.city = city
        self.balance = balance

    def __str__(self):
        return f'{self.name}{self.last_name}. {self.city}. Баланс: {self.balance} руб.'

    def guest(self):
        return f'{self.name}{self.last_name}, {self.city}'


cl1 = Client('Иван ', 'Петров', 'Москва', 50)
cl2 = Client('Федор ', 'Кузнецов', 'Псков', 70)
cl3 = Client('Фекла ', 'Ватутина', 'Суздаль', 25)
cl4 = Client('Марфа ', 'Андреева', 'Гдов', 47)


guest_list = [cl1, cl2, cl3, cl4]

print('Список гостей:\n')
for person in guest_list:
    print(person.guest())
