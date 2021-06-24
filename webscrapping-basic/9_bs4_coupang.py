# https://www.coupang.com/np/
# search?q=노트북&channel=user&component=&eventCategory=SRP
# &trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=
# &priceRange=&filterType=&listSize=36&filter=
# &isPriceRange=false&brand=&offerCondition=&rating=0
# &page=2&rocketAll=false&searchIndexingToken=1=5
# &backgroundColor=

import requests
import re
from bs4 import BeautifulSoup

url = "https://www.coupang.com/np/search?q=노트북&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=1=5&backgroundColor="
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1 Safari/605.1.15"}
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

items_cnt = 1
items = soup.find_all("li", attrs={"class":re.compile("^search-product")})
# print(items[0].find("div",attrs={"class":"name"}).get_text())
for item in items:
    # 광고 제품은 제외
    ad_badge = item.find("span",attrs={"class":re.compile("^ad-badge")})
    if ad_badge:
        name = item.find("div",attrs={"class":"name"}).get_text()
        print("Ad product will be not shown!! ")
        continue
    

    name = item.find("div",attrs={"class":"name"}).get_text()

    # 애플 제품 제외
    if "Apple" in name:
        print("Apple product will not be shown !!")
        continue

    price = item.find("strong",attrs={"class":"price-value"}).get_text()

    # 리뷰 100개 이상, 평점 4.5 이상 되는것만 조회

    rating = item.find("em",attrs={"class":"rating"})
    if rating:
        rating = rating.get_text()
    else:
        rating = "None"
        name = item.find("div",attrs={"class":"name"}).get_text()
        print("No rating production will not be counted !! ")
        continue

    rating_count = item.find("span",attrs={"class":"rating-total-count"})
    if rating_count:
        rating_count = rating_count.get_text() # (26) 이런식으로 넘어옴.. ()를 없앨려면 
        rating_count = rating_count[1:-1]
    else:
        rating_count = "None"
        name = item.find("div",attrs={"class":"name"}).get_text()
        print("No rating production will not be counted !! ")
        continue

    if float(rating) > 4.5 and int(rating_count) > 100:
        print("cnt"+ str(items_cnt) + "---------------")
        print("Notebook is ", name,price,rating, rating_count)
        print("---------------------------------------")
        items_cnt += 1

    