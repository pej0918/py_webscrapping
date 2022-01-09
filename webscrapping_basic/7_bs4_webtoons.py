import requests
from bs4 import BeautifulSoup

url="https://comic.naver.com/webtoon/weekday"
res=requests.get(url)
res.raise_for_status()

soup=BeautifulSoup(res.text, "lxml")

#soup객체에서 태그명이 a이고 class속성이 title인 모든 객체 반환
cartoons=soup.find_all("a",attrs={"class":"title"})
#find랑 find_all은 조건에 해당하는 첫번째 객체를 반환하냐 아니면 모든 객체를 반환하냐 그 차이이다.

#네이버 웹툰 전체 목록 가져오기
for cartoon in cartoons:
    print(cartoon.get_text().strip())

