import requests
from bs4 import BeautifulSoup

url="https://comic.naver.com/webtoon/weekday"
res=requests.get(url)
res.raise_for_status()

#request를 통해 가져온 html문서를 lxml parser를 통해 bs4객체로 가져옴
soup=BeautifulSoup(res.text,"lxml")

#get_text()를 통해서 각 객체의 text를 가져올 수 있다
#print(soup.a.get_text())
#print(soup.title.get_text())

print(soup.a.attrs)#a element 속성 정보를 반환
#객체의 속성 정보를 가져올 때는 []이용

print(soup.a["href"]) #a element의 속성 값 정보 출력
#print(soup.a)#soup 객체에서 처음 발견되는 a element 반환

#class="Nbtn_upload"인 a element 를 찾아줘
#print(soup.find("a", attrs={"class":"Nbtn_upload"}))
#class="Nbtn_upload"인 어떤 element를 찾아줘
#print(sou.find(attrs={"class":"Nbtn_upload"}))

#print(soup.find("li", attrs={"class":"rank01"}))

rank1=soup.find("li", attrs={"class":"rank01"})
#print(rank1.a.get_text())

#rank1다음 element 출력
#print(rank1.next_sibling.get_text()) #next_sibling했을 때 아무것도 출력이 안될경우 element간의 줄바꿈이 있을 경우임 그럴땐 한번더 해줌
#print(rank1.next_sibling.next_sibling.get_text())

#rank2=rank1.next_sibling.next_sibling
#print(rank2.get_text())
#rank3=rank2.next_sibling.next_sibling
#print(rank3.get_text())
# 이전 element는 previous_sibling으로 알 수 있음
#rank2=rank3.previous_sibling.previous_sibling
#print(rank2.get_text())

#부모 찾기
#print(rank1.parent)

#element간의 줄바꿈이 있는지 잘 모를 때
rank2=rank1.find_next_sibling("li") #li element 출력(next sibling)
print(rank2.get_text())
rank3=rank2.find_next_sibling("li")
print(rank3.get_text())
rank2=rank3.find_previous_sibling("li")
print(rank2.get_text())

#형제가 여러개 있을 때 한꺼번에 가져오기
print(rank1.find_next_siblings("li")) #rank1의 siblings가져오기

#<a onclick="nclk_v2(event,'rnk*p.cont','736277','1')" href="/webtoon/detail?titleId=736277&amp;no=113" title="싸움독학-113화 : 진짜 칼이네?!"> 싸움독학-113화 : 진짜 칼이네?!</a>
# <a...>"text"</a> : 

#a태그인데 text가 싸움독학...인 객체 가져오기
webtoon=soup.find("a",text="싸움독학-113화 : 진짜 칼이네?!")
print(webtoon)

