#네이버 코스피 시가 총액 순위정보를 csv형태로 저장

import csv #csv형태로 저장하기 위한 준비작업
import requests
from bs4 import BeautifulSoup

#url 맨마지막 부분에(page= 뒷부분) 원하는 페이지 수 넣어주면 그에 해당하는 페이지로 이동
url="https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page="

filename="시가총액1-200.csv"
#newline을 적용하지 않으면 줄과 줄 사이 공백 생김
#따라서 newline을 공백으로 설정
f=open(filename, "w",encoding="utf-8",newline="")
writer=csv.writer(f)

#탭으로 구분하여 각 문자열을 리스트에 저장
title="N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE".split("\t")
writer.writerow(title)

for page in range(1,5):#page1~4까지 
    res=requests.get(url + str(page))
    res.raise_for_status()
    soup=BeautifulSoup(res.text,"lxml")

    #코스피 테이블 가져오기
    data_rows=soup.find("table",attrs={"class":"type_2"}).find("tbody").find_all("tr")

    for row in data_rows:
        columns=row.find_all("td")
        #중간에 있는 빈 줄은 skip
        if len(columns)<=1:
            continue
        else:
            data=[column.get_text().strip() for column in columns]
            #print(data)
            writer.writerow(data)

#csv로 data 저장하는 법
#1.import csv:csv 불러오기
#2.filename=".csv": 파일 이름 지정
#3.f=open("filename","w",encoding="utf-8",newline=""):data를 file에 저장
#4.writer=csv.writer(f):파일을 csv형태로 저장하는 객체 생성
#5.writer.writerow(data):