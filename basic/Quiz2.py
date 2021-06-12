#추첨 프로그램

#조건 1 : 댓글은 20명이 작성하였고 아이디는 1-20이라고 가정
#조건 2 : 댓글내용과 상관없이 무작위로 추첨. 중복불가
#조건 3 : random모듈의 shuffle과 sampled을 활용

#출력 예제
#-- 당첨자 발표 --
#치킨 당첨자 : 1
#커피 당첨자 : [2,3,4]
#-- 축합 합니다. --

from random import *
users = range(1,21) #1 ~ 21직전까지
print(type(users))

users = list(users)
print(type(users))

print(users)
shuffle(users)
print(users)

winners = sample(users,4) # 1 for chicken 3 for 

print("-- 당첨자 발표 -- ")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))
print("-- 축하합니다. -- ")

# my coding
# id_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# print(id_list)
# shuffle(id_list)
# print(id_list, type(id_list))

# win1 = sample(id_list,1)
# print(win1)

# win3 = sample(id_list,3)
# print(win3)
# id_list = set(id_list)
# print(id_list, type(id_list))

# id_list.remove(win1)
# print(id_list, type(id_list))



