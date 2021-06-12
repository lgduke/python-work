# 표준 체중을 구하는 프로그램
# 표준체중 : 각 개인의 키에 적당한 체중
# 성별에 따른공식
# 남자 : 키(m)*키(m)*22
# 여자 : 키(m)*키(m)*21

# 조건 1 : 표준 체중은 별도의 함수 내에서 계산
#         * 함수명 :   std_weight
#         * 전달값 :   키(height) 성별(gender)
# 조건 2 : 표준 체중은 소숫점 둘째자리까지 표시

#(출력 예제)
# 키 175cm 남자의 표준 체중은 67.38kg 입니다.

def std_weight(height, gender):
    if gender == "M":
        gd_weight = height*height*22
    elif gender == "F":
        gd_weight = height*height*21
    else:
        gd_weight = 0
        printf("Wrong gender")
    return(gd_weight)

gd_weight = 0
gender_ok = 0


while gender_ok == 0:
    gender = input("What is your gender? ")
    if gender == "M" :
        print("OK you are man")
        gender_ok = 1
    elif gender == "F" :
        print("OK you are woman ")
        gender_ok = 1
    else:
        print("Wrong Gender")

height = input("What is your height? ")
height = int(height)/100

gd_weight = round(std_weight(height, gender),2)
print("Standard weight of the {0} with {1} height is {2}".format(gender,height,gd_weight))