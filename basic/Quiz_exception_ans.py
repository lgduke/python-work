# 시스템 코드를 확인하고 적절한 예외처리 구문을 넣으시오
# 조건 1 : 1보다 작거나 숫자가 아닌 입력값이 들어올때는 ValueError로 처리
#         출력메시지 : "잘못된 값을 입력하였읍니다."
# 조건 2 : 대기 손님이 주문할수 있는 총 치킨량은 10마리로 한정
#         치킨 소진시 사용자 정의 에러(SoldOutError)를 발생시키고 프로그램 종료
#         출력 메시지 : "재고가 소진되어 더 이상 주문을 받지 않습니다."

##

class SoldOutError(Exception):
    def __init__(self, msg):
        self.msg = msg
    def __str__(self):
        return self.msg


chicken = 10
waiting = 1
while(True):
    try:
        print("남은 치킨 : {0}".format(chicken))
        order = int(input("치킨을 몇마리 주문하십니까? "))
        print(str(type(order)))
 
        if order > chicken: #남은 치킨보다 주문이 많을때
            print("재료가 부족합니다.")
        elif order <= 0:
            raise ValueError
        else:
            print("[대기번호 {0}] {1}마리 주문이 완료되었읍니다.".\
                format(waiting,order))
            waiting += 1
            chicken -= order

        if chicken == 0:
            raise SoldOutError(str(chicken))

    except ValueError:
        print("Error is occured. You entered wrong input. Only decimal ")

    except SoldOutError:
        print("재고가 소진되어 더 이상 주문을 받지 않습니다. {0}".\
        format(order))
        break





