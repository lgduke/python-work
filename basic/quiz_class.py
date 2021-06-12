# 출력예제
# 총 3대의 매물이 있읍니다.
# 강남 아파트 매태 10억 2010년
# 마포 오피스텔 전세 5억 2007년
# 송파 빌라 월세 500/50 2000년

# 코드
class House:
    #매물 초기화
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year

    #매물 정보 표시
    def show_details(self):
        print("location {0}".format(self.location), end=" ")
        print("house_type {0}".format(self.house_type), end=" ")
        print("deal_type {0}".format(self.deal_type), end=" ")
        print("price {0}".format(self.price), end=" ")
        print("completion_year {0}".format(self.completion_year))

H1 = House("강남","아파트","매매","10억", 2010)
H2 = House("마포","오피스텔","전세","5억", 2007)
H3 = House("송파","빌라","월세","500/50", 2010)

house_units = []
house_units.append(H1)
house_units.append(H2)
house_units.append(H3)
     
print("총 {0}대의 매물이 있읍니다".format(len(house_units)))
for unit in house_units:
    unit.show_details()
        