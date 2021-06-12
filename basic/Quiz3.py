#   택시 서비스
# 50명의 승객과 매칭기회, 총 탑승 승객수를 구하는 프로그램

#조건 1 : 승객별 운앵 소요시간 5분~50분 난수로 정해짐
#조건 2 : 당신은 소요시간 5분~15분 사이의 승객만 매칭

#예제
#[0] 1번째 손님(소요시간 : 15분)
#[ ] 2번재 손님(소요시간 : 50분)
# ..
#[ ] 50번째 손님(소요시간 : 16분)

#총 탑승승객 : 2명
from random import *
customer_cnt = 0
time = range(5,51)
for customer_no in range(1,51):
#    print("Customer id {0}".format(customer_no))
    customer_time = sample(time,1)
#    print("Custome {0} taken time is {1}".format(customer_no, customer_time))
    if 5 <= customer_time[0] <= 15:
        print("[0] {0}th customer(Riding time : {1} minutes".format(customer_no, customer_time))
        customer_cnt += 1
    else:
        print("[ ] {0}th customer(Riding time : {1} minutes".format(customer_no, customer_time))

print("total customer is {0}".format(customer_cnt))
