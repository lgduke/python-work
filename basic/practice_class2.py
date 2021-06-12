class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} Unit is created.".format(self.name))
        print("Health {0}, Attack {1}".format(self.hp, self.damage))

class AttackUnit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        # print("{0} Unit is created.".format(self.name))
        # print("Health {0}, Attack {1}".format(self.hp, self.damage))
    def attack(self, location):
        print("{0} : {1} toward attack [attack] {2}".\
        format(self.name, location, self.damage))
    def damaged(self, damage):
        print("{0} : as much {1} as damaged ".format(self.name, damage))
        self.hp -= damage
        print("{0} : Health after damgage : {1}".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : is destructed ".format(self.name))

firebat1 =  AttackUnit("Firebat", 50, 16)
firebat1.attack("5 clock")

firebat1.damaged(25)
firebat1.damaged(25)
