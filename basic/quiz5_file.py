#회사에서 매추 1회 작성해야 하는 보고서가 있다
#아래와 같이 줄력

# - ?? 주차 추간보고 -
# Dept :
# Name :
# summary of done : 

#1주차 부터 50주차 까지의 보고서 화일을 만드는 프로그램
#조건 : 파일명은 '1주차.txt' 형태로 만든다

seq_week = 1
cons_name = "th weekly report"
cons_context = "Dept : " + "\n" + "Name : " + "\n" + "summary of done : " + "\n"
# print(cons_context)
while seq_week < 6:
    file_name = str(seq_week)+"weekly.txt"
    weekly_name = "-  "+str(seq_week)+cons_name + "  -"
#    print(file_name)
#    print(weekly_name)
    weekly_file = open(file_name,"w",encoding="utf8")
    weekly_file.write(cons_context)
    weekly_file.close()
    seq_week += 1

