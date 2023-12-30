class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Manager(Person):

    is_boss = False

    def __init__(self, name, age, num_employees):
        super().__init__(name, age)
        self.num_employees = num_employees

    def determine_boss_status(self):
        if self.num_employees >= 10:
            self.is_boss = True
        print(self.is_boss)

m1 = Manager("Rui", 22, 2)
m1.determine_boss_status()
