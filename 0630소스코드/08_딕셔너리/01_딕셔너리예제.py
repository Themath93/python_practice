#딕셔너리 만들기

d = {1:'a'}
print(d) ;print(type(d))  #<class 'dict'>

# 딕셔너리에 요소(아이템) 추가
# 딕셔너리[새로추가될 아이템의 키] = 저장할 값
d[2] = 'b'
print(d)

print("----------------------------------")

# key는 문자도 가능
# 연락처 구성위해 딕셔너리 생성(이름, 전화번호 저장)
member = {'name':"홍길동",'phone':'01012341234'}
print(member) #{'name': '홍길동', 'phone': '01012341234'}

# 주소 아이템 추가
member['address'] = '서울'
print(member)

naver = {
    "name" : "naver",
    "url" : "www.naver.com",
    "userid" : "nv",
    "password" : "1234"
}
google = {
    "name" : "google",
    "url" : "www.google.com",
    "userid" : "gg",
    "password" : "1234"
}

print(naver)
print(google)

print("-------------------------------------------")
# keys()/values()/items()

print(naver.keys()) # list 구조 list가 dict_keys()로 감싸져있다.
print(naver.values())
print(naver.items()) # list 구조안에 튜플이 있는 상태로 반환된다.

print(type(naver.keys())) # <class 'dict_keys'>
print(type(naver.values())) # <class 'dict_values'>
print(type(naver.items())) # <class 'dict_items'>


print("-----------------------------------------------")

# 리스트로 변환 : list() 함수

to_list = list(naver.keys())
print(to_list) # ['name', 'url', 'userid', 'password']
print(type(to_list)) # <class 'list'>

to_tuple = tuple(naver.keys())
print(to_tuple) # ('name', 'url', 'userid', 'password')
print(type(to_tuple)) # <class 'tuple'>

print()

# 각 요소 출력
# dict_keys/ dict_values / dict_items 타입은 반복요소로 사용 가능
for key in naver.keys() :
    print(key)
for value in naver.values() :
    print(value)
for item in naver.items() :
    print(item)


print("--------------------------------------------")
# key로 value 찾기

print(naver["userid"])
print(naver.get("password"))

# 찾고자하는 key가 딕셔너리에 없으면

# print(naver['link'])
print(naver.get("link"))
# link키를 찾아서 있으면 값을 반환 없으면 없음을 반환
print(naver.get("link","몰랑"))

#존재여부만확인
print('link' in google)
print('link' not in google)

# 딕셔너리 함수 확인
my_dict = {}
print(dir(my_dict))

