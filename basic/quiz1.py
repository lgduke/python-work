# Quiz ) site별로 비빌번호 작성

# 예) http://naver.com
# rule1 : http:// 부분은 제외 -> naver.com
# rule2 : 처음만나는 점(.) 이후 부분은 제외 -> naver
# rule3 : 남은 글자중 처음 3자리. + 글자 갯수 + 글자내 'e' 갯수 + !
# 예) 생성된 비밀먼호 : nav51!

sentence = "http://naver.com"
index = sentence.index("//")
print(index)
sp = index + 2
print("site is " + sentence[sp:])

new_st = sentence[sp:]
print(new_st)

index2 = new_st.index(".")
print(index2)

new_st2=new_st[:index2]
print("name is " + new_st2)

pw1 = new_st2[:3]
pw2 = str(len(new_st2))
pw3 = str(new_st2.count("e"))
pw4 ="!"

print(pw1," ", pw2 , " ", pw3 , " ", pw4)
pwd = pw1+pw2+pw3+pw4

print(f"Password is {pwd}")