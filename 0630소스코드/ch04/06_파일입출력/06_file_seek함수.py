

print("---------- 파일 내에서 검색 : seek() ---------")
f = open('test2.txt','r',encoding='utf-8')
f.seek(0,0) #시작위치 : 0행 0열
# 파일 전체 readlines()로 읽기
lines = f.readlines()
print(lines)
# ['01234\n', 'abcde\n', '가나다라마']

# f.seek(1,0) # 시작위치 : 0행 1열에서 시작
# lines = f.readlines()
# print(lines)

# 한글은 2바이트 사용 확인필요
f.seek(6,0) # 시작위치 : 0행 7열에서 시작
lines = f.readlines()
print(lines)


f.close()
