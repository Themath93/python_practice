# 02_파일에쓰기

# 파일에 쓰기
# w 쓰기모드로 열고 파일 객체의 write() 함수로 출력값을 파일에 기록
# f.write(데이터)
# open() - write() - close()
# data = "hi" # 영문은 엔코딩 문제가 없다.
data = "안녕하세요."
f = open("file2.txt",'w',encoding='utf-8')
# 한글을 UTF-8로 엔코딩해줘야 한다. 현재의 나는 맥os라 크레상관없다.
f.write(data) # 파일에 data 쓰기
f.close() # 파일 닫기
