#정규식 라이브러리 불러오기
import re

# . :하나의 문자(줄바꿈 문자는 제외)
#즉, ca.e는 a와e사이 줄바꿈 문자를 제외한 어떠한 문자가 와도 된다라는 뜻(정규식)
#->cake, care등은 가능하지만 caffe는 안된다. 왜냐하면 두글자가 들어감

#re.compile(정규식)
p=re.compile("ca.e")

#정규식 모음
# + : +바로 앞의 문자가 1번이상 반복
#ex) ca+b : cab, caab, caaa.....b

# *: *바로 앞의 문자가 0번이상 반복
#ex)ca*b : cb,cab,caab, caaa....b

# ? : ?바로 앞의 문자가 있어도 되고 없어도 된다
#ex)ca?b : cb,cab

# {m,n} : {}바로 앞의 문자가 m~n회 반복
#ex)ca{2,5}b:caab,caaab,caaaab,caaaaab
#ex)ca{2}b:caab

# ^ :문자열의 시작
#ex)^de: desk,develop....

# $:문자열의 끝을 의미
#ex) se$ : increase,  decrease.... 

#p(정규식)와 주어진 문자열의 처음부터 매치가 되는지 검사
#match : 주어진 문자열의 처음부터 매치가 되는지 확인
m=p.match("case")
#careless도 매치가 되는 문자열이다.
#good care는 매치가 되는 문자열이 아님


#매치가 되면 case가출력이 되고, 안되면 에러 발생
#group은 매치가 된다면 매칭 된 문자열 출력
print(m.group())

def print_match(m):
    if m: #정규식과 매치가 되었다면
        print("m.group():", m.group()) #매칭이 된 문자열 출력
        print("m.string():", m.string) #입력받은 문자열을 그대로 출력
        print("m.start():", m.start()) #매칭되는 문자열의 시작 인덱스 반환
        print("m.end():", m.end()) #매칭된 문자열의 끝 인덱스 반환
        print("m.span():", m.span()) #매칭된 문자열의 시작과 끝 인덱스 반환
    else:#매칭이 안됐다면
        print("매칭 되지 않았습니다. ")

#seach : 주어진 문자열 중에 매치되는 것이 있는지 확인->첫번째로 발견된 문자열 반환
m1=p.search("good care cake")
m2=p.match("good care cake")
#good care같은 경우에는 care가 일치하니까 매치가 됨

print_match(m)
print("-----")
print_match(m1)
print("-----")
print_match(m2)
print("-----")

#findall : 매칭이 되는 모든 것들을 리스트 형태로 반환
lst=p.findall("good care cake") 
print(lst)
lst2=p.findall("choco cake")
print(lst2)


#최종정리
#1.import re :정규식 라이브러리를 불러옴
#2.p=re.compile("원하는 형태(정규식)")
#3.m=p.match("비교문자열") : 정규식 문자열과 비교 문자열의 처음부터 비교하여 매칭이 되는지 검사
#4-1. print(m.group()) :매칭이 되면 매칭이 된 문자열 반환
#4-2. print(m.string) : 입력 받은 문자열 그대로 반환
#4-3. print(m.start()) : 매칭이 되는 문자열의 첫번째 인덱스 반환
#4-4. print(m.end()) : 매칭이 된 문자열의 마지막 인덱스 반환
#4-5. print(m.span()) : 매칭이 된 문자열의 첫번째/마지막 인덱스 반환


#5.p.search("비교문자열") : 정규식과 매칭이 되는 문자열을 반환
#6. lst= p.findall("비교문자열") : 정규식과 매칭이 되는 모든 문자열을 리스트로 반환