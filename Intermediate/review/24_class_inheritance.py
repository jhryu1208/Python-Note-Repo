"""
ex1
"""

class parent:
    def parent_ability(self):
        print("Do parent ability")

class child(parent):
    def child_ability(self):
        print("Do child ability")

def main():
    s = child()
    s.parent_ability()
    s.child_ability()

main()

"""
ex2
"""

class father:
    def father_ability(self):
        print('Do father ability!')

class mother:
    def mother_ability(self):
        print('Do mother ability!')

class child(father, mother):
    def child_ability(self):
        print('Do child ability!')

def main():
    s = child()
    s.father_ability()
    s.mother_ability()
    s.child_ability()

main()

"""
ex3
"""

class father:
    def strong_ability(self):
        print('strong father')

class sun(father):
    def strong_ability(self):
        print('more stronger than fater')

def main():
    s = sun()
    s.strong_ability()

main()

"""
ex4
"""

class father:
    def strong_ability(self):
        print('strong father')

class sun(father):
    def strong_ability(self):
        print('more stronger than fater')
    def hide_strong_ability(self):
        super().strong_ability()

def main():
    s = sun()
    s.strong_ability()
    s.hide_strong_ability()

main()

"""
ex5
"""

class car:
    def __init__(self, id, f):
        self.id = id
        self.fuel = f
    def drive(self):
        self.fuel -= 10
    def add_fuel(self, f):
        self.fuel += f
    def show_info(self):
        print(f"id : {self.id}")
        print(f"fuel : {self.fuel}")

class truck(car):
    def __init__(self, id, f, c):
        super().__init__(id, f)
        self.cargo = c
    def add_cargo(self, c):
        self.cargo += c
    def show_info(self):
        super().show_info()
        print(f"cargo : {self.cargo}")

def main():
    s = truck('42럭5959', 0, 0)

    s.add_fuel(100)
    s.add_cargo(50)

    s.drive()
    s.show_info()

main()
