#회사에서 매추 1회 작성해야 하는 보고서가 있다
#아래와 같이 줄력

# - ?? 주차 추간보고 -
# Dept :
# Name :
# summary of done : 

#1주차 부터 50주차 까지의 보고서 화일을 만드는 프로그램
#조건 : 파일명은 '1주차.txt' 형태로 만든다

for i in range(1, 6):
    with open(str(i)+"weekly2.txt", "w", encoding="utf8") as report_file:
        report_file.write("- {0}th weekly report - ".format(i))
        report_file.write("\n Dept :  ")
        report_file.write("\n Name :  ")
        report_file.write("\n Summary of done : ")
        
