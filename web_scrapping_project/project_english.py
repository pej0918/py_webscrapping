import re
import requests
from bs4 import BeautifulSoup

def scrape_english():
    print("[오늘의 영어 회화]")
    url="https://www.hackers.co.kr/?c=s_eng/eng_contents/I_others_english&keywd=haceng_submain_lnb_eng_I_others_english&logger_kw=haceng_submain_lnb_eng_I_others_english"
    res=requests.get(url)
    res.raise_for_status()    
    soup = BeautifulSoup(res.text, "lxml")
    #정규표현식 사용
    sentences= soup.find_all("div", attrs={"id":re.compile("^conv_kor_t")})
    print("(영어지문)")
    for sentence in sentences[len(sentences)//2:]: #길이가 8이라고 가정했을 때 인덱스 기준4-7까지 출력
        print(sentence.get_text().strip())
    print("(한글지문)")
    for sentence in sentences[:len(sentences)//2]:
        print(sentence.get_text().strip())

if __name__=="__main__":
    scrape_english()