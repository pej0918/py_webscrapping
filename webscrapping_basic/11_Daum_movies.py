import requests
from bs4 import BeautifulSoup

#최근 5개년 영화(2016-2020)
for year in range(2016,2021):
    url="https://search.daum.net/search?w=tot&q={}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR".format(year)
    res=requests.get(url)
    res.raise_for_status()

    soup=BeautifulSoup(res.text,"lxml")

    #영화 이미지 링크 가져오기
    images=soup.find_all("img",attrs={"class":"thumb_img"})
    for index,image in enumerate(images):
        image_url=image["src"]
        if image_url.startswith("/"):
            image_url="https://search1.kakaocdn.net/thumb/R232x328.q85" + image_url
        
        print(image_url)
        #이미지 링크에 들어가서 정보 조회
        image_res=requests.get(image_url)
        image_res.raise_for_status()

        #wb는 바이너리로 읽기/ 이미지는 문자가 아니기 때문
        #이렇게하면 모든 이미지를 가져와서 저장
        with open("movie_{}_{}.jpg".format(year,index+1),"wb") as f:
            f.write(image_res.content) #이미지 저장(content가 이미지를 의미)

        #상위 5개 파일의 이미지만 다운로드
        if index>=4:
            break