import requests
from bs4 import BeautifulSoup

url="https://comic.naver.com/webtoon/list?titleId=774862"
res=requests.get(url)
res.raise_for_status()

soup=BeautifulSoup(res.text,"lxml")

cartoons=soup.find_all("td",attrs={"class":"title"})
#find_all은 모든 객체를 리스트 형태로 저장
#따라서 각각의 객체에 접근하려면 리스트로 접근해야 한다
cartoon=cartoons[0].a.get_text().strip()#cartoons의 첫번째 요소의 a태그의 text출력
print(cartoon)
print("---------------------")
#페이지에 보이는 조조코믹스 최근화들의 제목과 해당되는 링크 스크래핑
for cartoon in cartoons:
    title=cartoon.a.get_text().strip()
    link=cartoon.a['href']
    print("{} : {}".format(title,"https://comic.naver.com"+link))

#평점 스크래핑
scores=soup.find_all("div",attrs={'class':'rating_type'})

total_scores=0
for score in scores:
    rate=score.strong.get_text()
    total_scores+=float(rate)
    print(rate)

print("전체 합계 평점 :",total_scores)
print("평균 평점 :",total_scores/len(scores))