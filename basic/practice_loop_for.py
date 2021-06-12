# print("Waiting No : 1")
# print("Waiting No : 2")
# print("Waiting No : 3")

waiting_no: int
# for waiting_no in [0,1,2,3,4]:
#     print("Waiting No : {0}".format(waiting_no))

for waiting_no in range(4):
    print("Waiting No : {0}".format(waiting_no))

for waiting_no in range(1,4):
    print("Waiting No : {0}".format(waiting_no))

starbucks = ["Ironman","Tor","IamGrut"]
for customer in starbucks:
    print("{0}, Coffee is ready".format(customer))

#while
customer ="Tor2"
index = 5
while index >= 1:
    print("{0}, Coffee is ready. {1} times left".format(customer,index))
    index -= 1
    if index == 0:
        print("Coffee is throw away")


customer ="Tor"
person ="Unknown"
index = 0

while person != customer :
    print("{0}, Coffee is ready. Call {1}".format(customer, index))
    index += 1
    person = input("What is your name? ")

# continue , break
absent = [2,5]
no_book = [7]
for student in range(1,11):
    if student in absent:
        continue #while 의 다음 반복으로 넘어감. 아래문장은 실행되지 않음
    if student in no_book:
        print("Class is over. {0} should go to teacher room".format(student))
        break #while 문이 끝남. 
    print("{0}, Read the Book".format(student))

# 1 line for
students = [1,2,3,4,5]
print(students)
students = [i+100 for i in students]
print(students)

# name length. 이름을 길이로 변환
students = ["Iron man","Thor","I am groot"]
students_len = [len(i) for i in students]
print(students)
print(students_len)

# name length. 이름을 대문자로 변환

students_Up = [i.upper() for i in students]
print(students)
print(students_Up)