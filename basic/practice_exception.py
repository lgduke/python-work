try: 
    print("나누기 전용 계산기입니다.")
    num1 = int(input("첫번째 숫자를 입력하세요 : "))
    num2 = int(input("두번째 숫자를 입력하세요 : "))
    print("{0} / {1} = {2}".format(num1,num2, int(num1/num2)))
except ValueError:
   print("Error is occured. You entered wrong input")
except ZeroDivisionError as err:
    print(err)