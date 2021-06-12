# travel package , thailand module 
# import 시에는 모듈까지만 가능하다. class는 안됨
# import travel.thailand.ThailandPackage --> 이건 오류남

# import travel.thailand

# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()


# from travel.thailand import ThailandPackage
# trip_to = ThailandPackage()
# trip_to.detail()


# from travel import vietnam
# trip_to2 = vietnam.VietnamePackage()
# trip_to2.detail()

from travel import *
# trip_to2 = vietnam.VietnamePackage()
# trip_to3 = thailand.ThailandPackage()

# trip_to2.detail()
# trip_to3.detail()

# 패키지가 어디에 있는지 찾아서 import 함
import inspect
import random
print(inspect.getfile(random))
print(inspect.getfile(vietnam))

