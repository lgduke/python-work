# 다중상속은 부모가 2이상. 부모 class, 자식 class 
# General Unit 

class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".\
            format(self.name, location, self.speed))
    

# Attack unit. from general unit

class AttackUnit(Unit): # Unit class를 상속받아서 Attack unit을 만듬
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self,name,hp, speed)
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
        AttackUnit.__init__(self, name, hp, 0, damage) #지상 스피드는 0으로 
        Flyable.__init__(self,flying_speed)
    
    # 오버라이딩 함수 정의
    def move(self,location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

# 벌쳐 : 지상유닛, 기동성이 좋음. 
vulture = AttackUnit("Vulture", 80, 10, 20)

# 베틀크루져 : 공중 유닛, 체력, 공격력 좋음
battlecruiser = FlyableAttackUnit("Battle Cruiser", 500, 25, 3)

vulture.move("11시")
#battlecruiser.fly("Battle Cruiser","9시")

# 지상, 공중유닛 공히 같은 함수 move를 쓰고 싶다. 그래서 overriding 한다
battlecruiser.move("9시")
