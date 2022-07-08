# 파일에 여러행 쓰기
# 1. \n 으로 여러행 만들기
# 2. 여러행으로 표시될 문자열을 생성해서 문자열 하나를 내보낸다.
# 1. write()는 한번만 사용

f = open("file3.txt",'w',encoding='utf-8')

# for i in range(1,11) :
#     data = '%d행\n' % i
#     f.write(data)

# 위 아래 방법은 같은 wirte 기능수행

data = ''
for i in range(1,11) :
    data = data + '%d행\n' % i
f.write(data)
f.close()



