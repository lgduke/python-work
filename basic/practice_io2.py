# 빈자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
print("{0: >10}".format(500))
#  양수일땐 +로 표시, 음수 일땐 - 로 표시
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))
#왼쪽 정렬하고 빈칸을 _로 채움
print("{0:_<+10}".format(500))
#3자리 마다 콤마를 찍어주기
print("{0:,}".format(10000000000000))
#3자리 마다 콤마를 찍어주기, +,- 부호도 붙이기
print("{0:+,}".format(10000000000000))
#3자리 마다 콤마를 찍어주기, +,- 부호도 붙이기, 자릿수 확보하고
#돈이 많으면 행복하니 빈자리는 ^

# ^로 가득채우고 왼쪽정렬을 하고 +를 통해서 부호를 붙이고 총 30만큼 공간을 확보하고 
# 3자리마다 , 를 찍어준다 
print("{0:^<+30,}".format(10000000000000))
# ^로 가득채우고 오른쪽정렬을 하고 +를 통해서 부호를 붙이고 총 30만큼 공간을 확보하고 
# 3자리마다 , 를 찍어준다 
print("{0:^>+30,}".format(10000000000000))

#소수점 출력
print("{0:f}".format(5/3))
# 소수점을 특정 자리수까지만 보고싶어
# 2자리 수 까지
print("{0:.2f}".format(5/3))
