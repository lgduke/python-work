

import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list.nhn?titleId=675554"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

# 네이버 웹툰 전체 목록 가져오기
g_cartoons_titles = soup.find_all("td",attrs={"class":"title"})
# Class 속성이 title인 모든 "a" element를 반환
# title  = g_cartoons[0].a.get_text()
# link = g_cartoons[0].a["href"]
# print(title)
# print("https://comic.naver.com" + link)

# for g_cartoon in g_cartoons:
#     title  = g_cartoon.a.get_text()
#     link = "https://comic.naver.com" + g_cartoon.a["href"]
#     print(title,link)

# 평점 구하기
total_rates = 0
g_cartoons = soup.find_all("div",attrs={"class":"rating_type"})
for g_cartoon in g_cartoons :
    rate = g_cartoon.find("strong").get_text()
    total_rates += float(rate)
    print(rate)

print("total rates is ", total_rates)
print("average rate is ", total_rates/len(g_cartoons))


# <a 
# href="/webtoon/detail.nhn?titleId=675554&amp;no=911&amp;weekday=mon" 
# onclick="nclk_v2(event,'lst.img','675554','911')">						
# <img src="https://shared-comic.pstatic.net/thumb/webtoon/675554/911/thumbnail_202x120_bcf9aa34-e246-42fd-a55e-f17825849283.jpg" 
# title="후기 + 10년 후 가우스" alt="후기 + 10년 후 가우스" 
# width="71" height="41" 
# onerror="this.src='https://ssl.pstatic.net/static/comic/images/migration/common/non71_41.gif'">
# <span class="mask"></span>
# 					</a>