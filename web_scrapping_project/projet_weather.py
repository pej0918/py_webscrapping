import requests
from bs4 import BeautifulSoup

def scrape_weather():
    print("[오늘의 인천 가좌2동 날씨]")
    url="https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%9D%B8%EC%B2%9C+%EA%B0%80%EC%A2%8C2%EB%8F%99+%EB%82%A0%EC%94%A8&oquery=%EC%9D%B8%EC%B2%9C+%EA%B0%80%EC%A2%8C%EB%8F%99+%EB%82%A0%EC%94%A8&tqi=hOPFRsprvxsssfkjNN4sssssscd-293856"
    res=requests.get(url)
    res.raise_for_status()
    soup=BeautifulSoup(res.text,"lxml")
    #어제보다 몇도 낮아요(높아요)
    cast=soup.find("p",attrs={"class":"summary"}).get_text().replace(soup.find("span",attrs={"class":"weather before_slash"}).get_text(),"")
    #현재 00도(최고/최저)
    curr_temp=soup.find("div",attrs={"class":"temperature_text"}).get_text().strip()
    min_temp=soup.find("span", attrs={"class":"lowest"}).get_text()
    max_temp=soup.find("span",attrs={"class":"highest"}).get_text()
    #오전/오후 강수확률
    morning_rain_rate=soup.find("span", attrs={"class":"weather_left"}).get_text().strip()
    middle=soup.find("span", attrs={"class":"weather_inner"})
    after=middle.find_next_sibling("span")
    afternoon_rain_rate=after.find("span", attrs={"class":"weather_left"}).get_text().strip()
    #미세먼지/초미세먼지
    dust=soup.find("ul", attrs={"class":"today_chart_list"})
    #find_all("class"):class이름이 class인 모든 element 반환/ 만약 뒤에[i]가 있으면 그 중 i번째 요소 반환하라는 뜻
    pm10=dust.find_all("li")[0].get_text().strip()#미세먼지
    pm25=dust.find_all("li")[1].get_text().strip()#초미세먼지

    print(cast)
    print(curr_temp,"("+min_temp,"/",max_temp+")")
    print("강수확률: {} {}".format(morning_rain_rate,afternoon_rain_rate))
    print(pm10,"/",pm25)

if __name__=="__main__":
    scrape_weather() #오늘의 날씨 정보 가져오기
