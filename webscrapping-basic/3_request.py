import requests
# res = requests.get("http://naver.com")
res = requests.get("http://google.com")

res.raise_for_status() #문제가 생길시 바로 stop
# print("Web scrapping is proceeded")
# # res = requests.get("http://nadocoding.tistory.com")
# # res = requests.get("http://naverrr.com")
# print("response code : ", res.status_code) # 200 is normal, 403 접근권한 없음

# if res.status_code == requests.codes.ok:
#     print("It is normal")
# else:
#     print("There is problem. [Error Code ",res.status_code,"]")

print(len(res.text))

with open("mygoogle.html","w", encoding="utf8") as f:
    f.write(res.text)

print("END")