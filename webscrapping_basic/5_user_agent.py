import requests
url="http://nadocoding.tistory.com"

#user agent: HTTP 요청을 보내는 디바이스와 브라우저 등 사용자 소프트웨어의 식별 정보를 담고 있는 request header의 한 종류이다. 
#크롬과 인터넷 익스플로어의 user agent는 다름
headers={"User-Agent ":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}
res=requests.get(url)

with open("nadocoding.html", "w", encoding="utf8") as f:
    f.write(res.text)