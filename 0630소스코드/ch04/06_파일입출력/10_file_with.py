# with문으로 파일열기

with open('test3.txt','w') as f :
    f.write("hello")

# with 문 사용하면 close()는 따로 하지 않아도 자동 종료

# 파일명은 변수로 사용 가능
file = "text4.txt"
data = '''Python programming
R programming
web programming'''

with open(file, 'w') as f:
    f.write(data)