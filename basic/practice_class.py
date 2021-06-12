class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} Unit is created.".format(self.name))
        print("Health {0}, Attack {1}".format(self.hp, self.damage))

marine1 = Unit("Marine", 40, 5)
marine2 = Unit("Marine", 40, 5)
tank = Unit("Tank", 150, 35)

wraith1 = Unit("Wraith", 150, 35)
print("Unit name is {0}.,Health {1}, Attack {2}".format(wraith1.name, wraith1.hp, wraith1.damage))
 
wraith2 = Unit("Taken Wraith", 150, 35)
wraith2.clocking = True

if wraith2.clocking == True:
    print("{0} is cloaked ".format(wraith2.name))

# # starcraft 
# # 마린 : 공격 유닛, 군인, 총을 쏠수 있음

# name = "marine" # name of unit
# hp = 40 # health of unit
# damage = 5 # attack of unit

# print("{0} unit is created".format(name))
# print("Health {0}, Attack {1}\n".format(hp,damage))

# # 탱그 : 공격 유닛, 탱그, 포를 쓰는데 일반모드, 시즈모드 
# tank_name = "Tank"
# tank_hp = 150
# tank_damage = 35

# print("{0} unit is created".format(tank_name))
# print("Health {0}, Attack {1}\n".format(tank_hp,tank_damage))

# # 탱그 2: 공격 유닛, 탱그, 포를 쓰는데 일반모드, 시즈모드 
# tank2_name = "Tank2"
# tank2_hp = 150
# tank2_damage = 35

# print("{0} unit is created".format(tank2_name))
# print("Health {0}, Attack {1}\n".format(tank2_hp,tank2_damage))

# def attack(name, location, damage):
#     print("{0} : {1}방향으로 적군을 공격합니다. [공격력 {2}]".format( \
#         name,location,damage))

# attack(name,"1시",damage)
# attack(tank_name,"1시",tank_damage)

