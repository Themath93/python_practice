# 파일내에 입력된 문자가 있는지 확인하는 예제
# read() 사용

f = open('test2.txt','r',encoding='utf-8')
data = f.read()
f.close()

value = input("검색 값 입력 : ")

if value in data :
    print("데이터가 있습니다.")
else:
    print("데이터가 없습니다.")
