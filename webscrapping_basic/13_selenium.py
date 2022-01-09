from selenium import webdriver


#chrome webdriver 객체, browser생성
browser= webdriver.Chrome("C:/Users/samsung/Desktop/webscrapping/chromedriver.exe")#괄호 안에 크롬드라이버가 있는 경로를 써줘야 함
#그 객체(browser)에서 naver로 접근
browser.get("https://naver.com") #chrome에서 네이버를 열어준다

#네이버 로그인버튼에 접근(beautifulsoup와 같은 방식으로 접근)
elem=browser.find_element_by_class_name("link_login") #class name으로 찾기
elem.click()#네이버 로그인버튼 클릭

#id와 pw입력하기
browser.find_element_by_id("id").send_keys("naver_id")#아이디 입력
browser.find_element_by_id("pw").send_keys("naver_pw")#비밀번호입력
browser.find_element_by_class_name("btn_text").click()#로그인버튼 클릭

#새로운 id 입력
browser.find_element_by_id("id").clear #기존에 있던 id를 지운다
browser.find_element_by_id("id").send_keys("my_id") #그러고 나서 새로운 id입력

#html정보 출력
print(browser.page_source)

#브라우저 종료
browser.close()#현재 탭만 종료
browser.quit()#전체 브라우저 종료

browser.back()#이전화면으로 돌아가기
browser.forward()#다시 앞화면으로 돌아가기
browser.refresh()#새로고침하기

#검색창 접근
elem=browser.find_element_by_id("query")#id로 찾기
#검색창에 검색하기 위한(엔터버튼을 누르기위한) 준비 작업
from selenium.webdriver.common.keys import Keys
#검색창에 나도코딩 입력
elem.send_keys("나도코딩")
#엔터버튼 클릭
elem.send_keys(Keys.ENTER)

#요소 여러개 가져오고 싶을 때는 elements를 쓰면 된다
elems=browser.find_elements_by_tag_name("a")#태그 이름이 a인 요소 전부 가져오기
for elem in elems:
    #href속성 가져오기(beautifulsoup에서는 a["href"]이런식으로 가져왔음)
    elem.get_attribute("href")

#다른 페이지로 이동(네이버에서 다음페이지로 이동)
browser.get("http://daum.net")
#검색창에 검색어 입력
elem=browser.find_element_by_name("q")
elem.send_keys("나도코딩")
#엔터버튼 클릭
elem.send_keys(Keys.ENTER)
browser.back()
#검색어 입력
elem=browser.find_element_by_name("q")
elem.send_keys("나도코딩")
#이번에는 xpath로 검색버튼 접근해서 검색버튼 클릭
elem=browser.find_element_by_xpath("//*[@id='daumSearch']/fieldset/div/div/button[2]")
elem.click()

#현재 탭 닫기
browser.close()
#모든 탭 닫기
browser.quit()
