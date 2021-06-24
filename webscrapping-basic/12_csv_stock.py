import csv
import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page="
filename = "market_cap1-200.csv"
f = open(filename,"w", encoding="utf-8-sig", newline="")
writer=csv.writer(f)

title = "N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE".split("\t")
print(type(title))
writer.writerow(title)

for page in range(1,13):
    res=requests.get(url+str(page))
    res.raise_for_status()
    soup = BeautifulSoup(res.text,"lxml") #parser는 lxml로 함

    data_rows = soup.find("table", attrs={"class":"type_2"}).\
        find("tbody").find_all("tr")
    for row in data_rows:
        columns = row.find_all("td")
        if len(columns) <= 1:
            continue
        data = [column.get_text().strip() for column in columns] 
        #strip() 불필요한 캐릭터 제거
        # print(data) 
        writer.writerow(data)