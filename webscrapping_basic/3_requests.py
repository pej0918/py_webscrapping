# request를 통해 웹페이지정보를 추출

import requests
res=requests.get("http://naver.com")

 #200이면 정상
 #즉, 이 페이지에 대한 접근권한이 있고, 웹스크래핑을 할 수 있다는 뜻
print("응답코드", res.status_code)

# res1에 해당되는 url은 없는 페이지이므로, 응답코드를 출력하면 200이 아닌 다른 숫자가 나오게 된다.
# 이 페이지에 대한 접근권한이 없다는 뜻
res1=requests.get("http://eunjustudy.tistory.com")
print("응답코드1", res1.status_code)

if res.status_code==requests.codes.ok : #res.status_code가 정상(즉,200)이면
    print("정상입니다") #200이면 출력
else: #200이 아닌 다른 숫자면 출력
    print("문제가 생겼습니다. [에러코드", res.status_code,"]")

if res1.status_code==requests.codes.ok :
    print("정상입니다")
else:
    print("문제가 생겼습니다. [에러코드", res1.status_code,"]")


#아예 에러를 발생시키는 법
res.raise_for_status()
print("에러가 발생하게 된다면 이 문장은 출력이 안됩니다")


print(len(res.text))
print(res.text)

#파일 생성
#form: 파일객체=open(파일이름, 파일열기모드)
#form2: with open(파일이름, 파일읽기모드) as 파일객체
#파일열기모드: r-파일을 읽을 때/ w-파일에 내용을 쓸 때/ a-파일의 마지막에 새로운 내용을 추가 시킬 때

with open("mygoogle.html", "w", encoding="utf8") as f:
    #write를 통해 파일에 새로운 내용 추가할 수 있음
    #만약 파일읽기모드가 a인 상태에서 사용하면 내용이 추가되지만
    #w인 상태에서 사용하면 원래가지고 있던 내용이 다 삭제된 후 새롭게 추가된다.
    f.write(res.text)