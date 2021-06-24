# regular expression example
#주민번호
#[]
#이메일 주소
#차량번호
#123가 1234
#IP 주소
#192.168.0.1

# 사용방법
# 1. p=re.compile("원하는 정규표현식")
# 2. m=p.match("비교할 문자열 ")
# 3. m = p.search("비교할 문자열") # 주어진 문자열중에 일치하는게 있는지 확인
# 4. lst = p.findall("비교할 문자열") 
# # findall : 일치하는 모든것을 리스트 형태로 반환

# 원하는 정규 표현식
# .(ca.e) : 하나의 문자를 의미 - care, cafe, case ...
# ^ (^de) : 문자열의 시작 - desk, destination.. | fade(X)
# $ (se$) : 문자열의 끝 - case, base

import re
#차량번호 abcd, book 등 4개의 문자로 구성되었다고 가정
#ca?e 

p = re.compile("ca.e") 
# .(ca.e) : 하나의 문자를 의미 - care, cafe, case ...
# ^ (^de) : 문자열의 시작 - desk, destination.. | fade(X)
# $ (se$) : 문자열의 끝 - case, base

def print_match(m):
    # m = p.match("caffe")
    # print(m.group()) #매치되지 않으면 에러가 발생
    if m:
        print("---------")
        print("m.group() : ", m.group()) #일치하는 문자열을 반환
        print("m.string : " , m.string) # 입력받은 문자열을 출력
        print("m.start : ", m.start()) # 일차하는 문자열의 시작 index
        print("m.end() : ",m.end()) #일치하는 문자열의 끝 index
        print("m.span()", m.span()) # 일치하는 문자열의 시작, 끝 index 함께 표현

    else:
        print("---------")
        print("No match")

# m = p.match("care")
# print_match(m)
# m = p.match("careless") # match : 주어진 문자열의 처음부터 일차하는지 확인
# print_match(m)
# m = p.match("case")
# print_match(m)
# m = p.match("caffe")
# print_match(m)


# m = p.search("careless") # 주어진 문자열중에 일치하는게 있는지 확인
# print_match(m)
# m = p.search("good care") # 주어진 문자열중에 일치하는게 있는지 확인
# print_match(m)

lst = p.findall("careless") # findall : 일치하는 모든것을 리스트 형태로 반환
print(lst)

lst = p.findall("good cafe") # findall : 일치하는 모든것을 리스트 형태로 반환
print(lst)

lst = p.findall("good care cafe") # findall : 일치하는 모든것을 리스트 형태로 반환
print(lst)
