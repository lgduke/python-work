# 다중상속은 부모가 2이상. 부모 class, 자식 class 
# General Unit 
class Unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
# Attack unit. from general unit

class AttackUnit(Unit): # Unit class를 상속받아서 Attack unit을 만듬
    def __init__(self, name, hp, damage):
        Unit.__init__(self,name,hp)
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

# 드랍쉽 : 공중유닛, 수송기, 공격기능 없음
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [speed {2}]".\
            format(name,location,self.flying_speed))

# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit,Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self,flying_speed)

# 발키리 : 공중공격 유닛, 한번에 14발 미사일 발사
valkyrie = FlyableAttackUnit("Valkyrie", 200,6,5)
valkyrie.fly(valkyrie.name, "1시" )