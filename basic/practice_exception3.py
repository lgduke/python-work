class BigNumberError(Exception):
    def __init__(self, msg):
        self.msg = msg
    def __str__(self):
        return self.msg


try:
    print("한자리 숫자 나누기 전용 계산기")
    num1 = int(input("첫번째 숫자를 입력하세요 : "))
    num2 = int(input("두번째 숫자를 입력하세요 : "))
    if num1 >= 10 or num2 >= 10:
        raise BigNumberError("Input Value : {0}, {1}".format(num1,num2))
    print("{0} / {1} = {2}".format(num1,num2, int(num1/num2)))
except ValueError:
   print("Error is occured. You entered wrong input. Only one digit")

except BigNumberError as err:
   print("Error is occured. Please Only one digit")
   print(err)

finally:
# 오류건 정상이건 무조건 실행되는 문장
    print("Thanks for using this utils")
