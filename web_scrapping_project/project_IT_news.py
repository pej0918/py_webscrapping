import requests
from bs4 import BeautifulSoup

def scrape_IT_news():
    print("[IT 뉴스]")
    url="https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid1=105&sid2=230"
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}
    res = requests.get(url, headers=headers)
    res.raise_for_status()    
    soup = BeautifulSoup(res.text, "lxml")
    news_list=soup.find("ul",attrs={"class":"type06_headline"}).find_all("li", limit=3) #3개의 기사만 가져오기
    for index,news in enumerate(news_list):
        #이미지가 없을 때는 첫번째 a태그 이미지가 있을 때는 두번째 a태그에서 가져와야 함(제목을)
        img=news.find("img")
        if img:
            title=news.find_all("a")[1].get_text().strip()
        else:
            title=news.find("a").get_text().strip()
        link=news.find("a")["href"]
        print("{}. {}".format(index+1, title))
        print("   (링크 : {})".format(link))




if __name__=="__main__":
    scrape_IT_news()