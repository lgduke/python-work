import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
# print(soup.title)
# print(soup.title.get_text())

# print(soup.a) # soup 객체중에 처음으로 발견되는 a element를 찾아서 프린트
# print(soup.a.attrs) # a element의 전체 속성을 출력
# print(soup.a["href"]) # a element의 href 속성값을 출력

# print(soup.find("a", attrs={"class":"Nbtn_upload"}))
# class값이 Nbtn_upload 인 a element를 찾아줘

# print(soup.find(attrs={"class":"Nbtn_upload"})) 
# class값이 Nbtn_upload 인 어떤 element를  찾아줘

# print(soup.find("li", attrs={"class":"rank01"}))
# rank1 = soup.find("li", attrs={"class":"rank01"})
# print(rank1.a)
# print("-----")
# print(rank1.a["href"])
# print(rank1.a.get_text())
# print(rank1.next_sibling)
# print(rank1.next_sibling.next_sibling)
# rank2 = rank1.next_sibling.next_sibling
# rank3 = rank2.next_sibling.next_sibling
# print(rank2.a.get_text())
# print(rank3.a.get_text())
# rank2 = rank3.previous_sibling.previous_sibling
# print(rank2.a.get_text())
# print(rank1.parent)

# print(rank1.a.get_text())
# rank2 = rank1.find_next_sibling("li")
# print(rank2.a.get_text())
# rank3 = rank2.find_next_sibling("li")
# print(rank3.a.get_text())
# rank4 = rank3.find_next_sibling("li")
# print(rank4.a.get_text())

# rank2 = rank3.find_previous_sibling("li")
# print(rank2.a.get_text())

# print(rank1.find_next_siblings("li")) 
# 한형제가 아니라 나머지 전체 형제들을 가지고 옴 

# <a 
# onclick="nclk_v2(event,'rnk*p.cont','748105','1')" 
# href="/webtoon/detail.nhn?titleId=748105&amp;no=101" 
# title="독립일기-100화 독립을 돌아보며">
# 여기까지 여는 테그임.
# 독립일기-100화 독립을 돌아보며
# 텍스트 
# </a>
# 닫는 태그

# a 태그 밑에 onclick , href, title 이 있음. 여는 태그 그 다음은 text 임

webtoon = soup.find("a", text="독립일기-100화 독립을 돌아보며")
print(webtoon)