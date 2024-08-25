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

h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)