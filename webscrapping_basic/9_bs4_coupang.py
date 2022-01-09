
#http method에는 대표적으로 get과 post가 있음
#get은 어떤 정보를 누구나 볼 수 있게 url에 게시
#post는 url이 아닌 http의 body에 숨김
#웹페이지에서 어떤 메뉴를 선택할 때 url이 바뀌면 get/안 바뀌면 post방식
#쿠팡은 get방식을 사용해서 우리가 쿠팡을 스크래핑할 수 있는 것

import requests
import re
from bs4 import BeautifulSoup

url="https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=1=5&backgroundColor="
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()    

soup = BeautifulSoup(res.text, "lxml")

#노트북 정보 가져오기
print("노트북 정보 조회")
items= soup.find_all("li",attrs={'class':re.compile('^search-product')})#class 속성값이 search-product로 시작하는 모든 li태그를 반환
#print(items[0].find("div",attrs={'class':'name'}).get_text().strip())
for item in items:
    name=item.find("div",attrs={"class":"name"}).get_text().strip()
    price=item.find("strong",attrs={"class":"price-value"}).get_text().strip()
    #평점이 없는 것도 있음(당연히 평점이 없으면 리뷰도 없음)
    rate=item.find("em",attrs={"class":"rating"})
    if rate:#평점이 있으면
        rate=rate.get_text().strip()
        reviews=item.find("span",attrs={"class":"rating-total-count"}).get_text().strip().replace("(","").replace(")","")
        print("{}\n가격 : {}원\n평점 : {}\n리뷰 개수 : {}".format(name,price,rate,reviews))
        print("\n")
    else:#평점이 없으면
        print("{}\n가격 : {}원".format(name,price))
        print("\n")

#광고제품을 제외한 노트북 정보 가져오기
print("광고제품 제외 노트북 조회")
items= soup.find_all("li",attrs={'class':re.compile('^search-product')})
for item in items:
    #광고 제품 여부 확인용 변수
    ad=item.find("span",attrs={"class":"ad-badge-text"})
    if ad: #광고제품이면
        continue #다음 반복문 실행
    else: #광고제품이 아니면
         name=item.find("div",attrs={"class":"name"}).get_text().strip()
         price=item.find("strong",attrs={"class":"price-value"}).get_text().strip()
         #평점이 없는 것도 있음(당연히 평점이 없으면 리뷰도 없음)
         rate=item.find("em",attrs={"class":"rating"})
         if rate:#평점이 있으면
             rate=rate.get_text().strip()
             reviews=item.find("span",attrs={"class":"rating-total-count"}).get_text().strip().replace("(","").replace(")","")
             print("{}\n가격 : {}원\n평점 : {}\n리뷰 개수 : {}".format(name,price,rate,reviews))
             print("\n")
         else:#평점이 없으면
            print("{}\n가격 : {}원".format(name,price))
            print("\n")


#리뷰100개 이상 평점 4.5이상인 것만 조회
print("리뷰100개 이상 평점 4.5이상 노트북 조회(광고 제외)")
items= soup.find_all("li",attrs={'class':re.compile('^search-product')})
for item in items:
    #광고 제품 여부 확인용 변수
    ad=item.find("span",attrs={"class":"ad-badge-text"})
    if ad: #광고제품이면
        continue #다음 반복문 실행
    else: #광고제품이 아니면
         name=item.find("div",attrs={"class":"name"}).get_text().strip()
         price=item.find("strong",attrs={"class":"price-value"}).get_text().strip()
         #평점이 없는 것도 있음(당연히 평점이 없으면 리뷰도 없음)
         rate=item.find("em",attrs={"class":"rating"})
         if rate:#평점이 있으면
             rate=rate.get_text().strip()
             reviews=item.find("span",attrs={"class":"rating-total-count"}).get_text().strip().replace("(","").replace(")","")
             #평점4.5이상 리뷰수100개 이상
             if (float(rate)>=4.5)and (float(reviews)>=100):
                 print("{}\n가격 : {}원\n평점 : {}\n리뷰 개수 : {}".format(name,price,rate,reviews))
                 print("\n")
             else:#평점/리뷰 조건 충족 못하면
                 continue #그냥 넘어가라
         else:#평점이 없으면
            print("{}\n가격 : {}원".format(name,price))
            print("\n")


print("Apple제품 제외")
#Apple제품 제외
items= soup.find_all("li",attrs={'class':re.compile('^search-product')})
for item in items:
    #광고 제품 여부 확인용 변수
    ad=item.find("span",attrs={"class":"ad-badge-text"})
    if ad: #광고제품이면
        continue #다음 반복문 실행
    else: #광고제품이 아니면
         name=item.find("div",attrs={"class":"name"}).get_text().strip()
         price=item.find("strong",attrs={"class":"price-value"}).get_text().strip()
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
                     print("{}\n가격 : {}원\n평점 : {}\n리뷰 개수 : {}".format(name,price,rate,reviews))
                     print("\n")
             else:#평점/리뷰 조건 충족 못하면
                 continue #그냥 넘어가라
         else:#평점이 없으면
            print("{}\n가격 : {}원".format(name,price))
            print("\n")