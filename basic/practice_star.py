# 다중상속은 부모가 2이상. 부모 class, 자식 class 
# General Unit 

from random import *

class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0} Unit is created.".format(name))
    def move(self, location):
#        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".\
            format(self.name, location, self.speed))
    def damaged(self, damage):
        print("{0} : as much {1} as damaged ".format(self.name, damage))
        self.hp -= damage
        print("{0} : Health after damgage : {1}".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : is destructed ".format(self.name))    

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

class Marine(AttackUnit):
    def __init__(self):
        super().__init__("Marine", 40, 1, 5)
    
    #stim pack : 일정시간 이동 공격속도를 증가. 자기체력 10 감소
    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print("{0} : Use stimpack(Decrase 10 Hp {1})".\
                format(self.name, self.hp))
        else:
            print("{0} : Hp is not enough {1}.".format(self.name, self.hp))

class Tank(AttackUnit):
    seize_developed = False

    def __init__(self):
        AttackUnit.__init__(self, "Tank", 150, 1, 35)
        self.seize_mode = False

    def set_seize_mode(self):
        if Tank.seize_developed == False:
            return
        
        # 시즈모드가 아닐때 시즈모드로 전환
        if self.seize_mode == False:
            print("{0} : Transfered to Seize Mode".format(self.name))
            self.damage *= 2
            self.seize_mode = True
        # 시즈모드일때 시즈모드 해제
        else:
            print("{0} : Transfered to Non Seize Mode".format(self.name))
            self.damage /= 2
            self.seize_mode = False
            




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
#       print("[공중 유닛 이동]")
        self.fly(self.name, location)

class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, "Wraith", 80, 20, 5)
        self.clocked = False 
    
    def clocking(self):
        if self.clocked == True:
            print("{0} : 클로킹 모드 해제합니다.".format(self.name))
            self.clocked = False
        else:
            print("{0} : 클로킹 모드 설정 합니다.".format(self.name))
            self.clocked = True

def game_start():
    print("[Alram] New Game begins")

def game_over():
    print("Player : GG ")
    print("[player] is out ")

# 실제 게임 진행
game_start()

# 마린 3기 생성
m1 = Marine()
m2 = Marine()
m3 = Marine()

t1 = Tank()
t2 = Tank()

w1 = Wraith()

# 유닛 일괄 관리
attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

#전군 이동
for unit in attack_units:
    unit.move("1시")

# 탱크 시즈모드 개발
Tank.seize_developed = True
print("[Alram] Tank Seize mode is developed")

#공격 모드 준비( 마린 : 스팀팩, 탱크 : 시즈모드 : 레이스 : 클로킹)
for unit in attack_units:
    if isinstance(unit, Marine):
        unit.stimpack()
    elif isinstance(unit, Tank):
        unit.set_seize_mode()
    elif isinstance(unit, Wraith):
        unit.clocking()


# Begin Attack

for unit in attack_units:
    unit.attack("1시")

#전군 피해
for unit in attack_units:
    unit.damaged(randint(5,21)) #공격은 랜덤. 5~21


#게임종료
game_over()
