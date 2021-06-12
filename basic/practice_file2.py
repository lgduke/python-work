# score_file = open("score.txt","r",encoding="utf8")
# print(score_file.read())
# score_file.close()

score_file = open("score.txt","r",encoding="utf8")
print(score_file.readline(), end="") #한줄읽고 커서를 다음줄로 이동
print(score_file.readline(), end="")
print(score_file.readline(), end="")
print(score_file.readline())
score_file.close()

score_file = open("score.txt","r",encoding="utf8")
while True:
    line = score_file.readline() #한줄읽고 커서를 다음줄로 이동
    if not line: 
        break
    print(line, end="")
print("")
print("")

score_file.close()

score_file = open("score.txt","r",encoding="utf8")
lines = score_file.readlines() #화일을 읽어와서 리스트 형태로 저장
for line in lines:
    print(line, end="")

score_file.close()

