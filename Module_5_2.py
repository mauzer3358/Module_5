class House:
    def __init__(self, name, number_of_flours):
        self.name = name
        self.number_of_flours = number_of_flours

    def go_to(self, new_flour):
        if new_flour < 1 or new_flour > self.number_of_flours:
            print('Такого этажа не существует')
        else:
            i = 1
            while i <= new_flour:
                print(i)
                i += 1

    def __len__(self):
        return self.number_of_flours

    def __str__(self):
        return f' Название: {self.name}, кол-во этажей: {self.number_of_flours}'

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))
