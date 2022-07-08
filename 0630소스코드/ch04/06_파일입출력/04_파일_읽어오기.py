# 04_파일_읽어오기.py

# readline()
print("---------- 첫번째 행 읽기 ----------")

f1 = open('test.txt', 'r')
# f1 = open('test.txt', 'r',encoding='utf-8') #한글이 깨질때는 이 매개변수 추가된 방식을 사용
line = f1.readline() # 첫번째 라인읽기
print(line)
f1.close()


print("================= 파일 전체 읽기 ====================")
# readlien()
# 1행씩 읽고 출력
f2 = open('test.txt', 'r')

# 해당 파일의 총 라인수를 알 수 없으므로 무한반복문시행
while True :
    line = f2.readline() # line 1개 읽고
    if not line : # 라인에 읽은 내용이 없으면
        break
    print(line,end='') # 읽어온 line 출력 , print 자체의 줄바꿈은 하지않는다.
    # 출력 결과는 두줄 간격으로 출력 : 원 데이터에서 줄바꿈도 같이 가져오기때문
print()
f2.close()
