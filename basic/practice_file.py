# score_file = open("score.txt","w",encoding="utf8" )
# print("Math : 0", file=score_file)
# print("English : 50", file=score_file)
# print("Math : 0")
# print("English : 50")
# score_file.close()

# w는 신규 생성 및 덮어쓰기. a는 추가 
score_file = open("score.txt","a",encoding="utf8" )
score_file.write("Science : 80 \n")
score_file.write("Coding : 100")
score_file.close()