class Unit:
    def __init__(self):
        print("Unit Creator")
class Flyable:
    def __init__(self):
        print("Flyable Creator")

# 2개 이상의 부모 Class를 다중 상속받을때
# super는 맨처음 호출되는 부모 class가 호출된다

class FlyableUnit(Flyable, Unit):
    def __init__(self):
#        super().__init__()
        Unit.__init__(self)
        Flyable.__init__(self)
# dropship
dropship = FlyableUnit()