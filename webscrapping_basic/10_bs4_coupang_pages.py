#페이지1뿐만 아니라 여러 페이지에 대한 노트북 조회

import requests
import re
from bs4 import BeautifulSoup

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}
#페이지1부터5까지 조회
for i in range(1,6):
    #i에 따라 "page=i"로 변하면서 1부터5페이지까지 조회할 수 있음
    url="https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={}&rocketAll=false&searchIndexingToken=1=5&backgroundColor=".format(i)
    res = requests.get(url, headers=headers)
    res.raise_for_status()    
    soup = BeautifulSoup(res.text, "lxml")
    items= soup.find_all("li",attrs={'class':re.compile('^search-product')})
    print("page{} 조회".format(i))
    for item in items:
        #광고 제품 여부 확인용 변수
        ad=item.find("span",attrs={"class":"ad-badge-text"})
        if ad: #광고제품이면
            continue #다음 반복문 실행
        else: #광고제품이 아니면
            name=item.find("div",attrs={"class":"name"}).get_text().strip()
            price=item.find("strong",attrs={"class":"price-value"}).get_text().strip()
            link=item.find("a",attrs={"class":"search-product-link"})["href"]
            #평점이 없는 것도 있음(당연히 평점이 없으면 리뷰도 없음)
            rate=item.find("em",attrs={"class":"rating"})
            if rate:#평점이 있으면
                rate=rate.get_text().strip()
                reviews=item.find("span",attrs={"class":"rating-total-count"}).get_text().strip().replace("(","").replace(")","")
                #평점4.5이상 리뷰수100개 이상
                if (float(rate)>=4.5)and (float(reviews)>=100):
                    if "Apple" in name: #이름에 Apple이 들어가면
                        continue 
                    else: #안 들어가면
                        print("{}\n가격 : {}원\n평점 : {}\n리뷰 개수 : {}\n링크 : {}".format(name,price,rate,reviews,"https://www.coupang.com" + link))
                        print("\n")
                else:#평점/리뷰 조건 충족 못하면
                    continue #그냥 넘어가라
            else:#평점이 없으면
                print("{}\n가격 : {}원\n링크 : {}".format(name,price,"https://www.coupang.com" + link))
                print("\n")