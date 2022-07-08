# 01.파일생성

# 파일을 쓰기 모드로 연다.
# 해당파일이 존재하면 덮어씀(기존내용사라짐)
# 해당파일이 존재하지 않으면 새로 생성

# 파일생성 : 파일명만 적으면 현재 디렉토리에 생성
# open(파일명,모드) : 실행 후 반환되는 파일 포인터를 반드시 저장해야 됨
# f = open("file1.txt","w")
# f.close() # 파일 닫기

# 메모장에 file1.txt 파일을 열고 내용 입력

# 이 파일 한번 실행 다시 실행 했을 때
# 같은 이름의 파일이 있어도 동일안 파일 생성 (덮어쓰기)


########################################################

# 파일 생성 (특정 디렉터리에 생성)
# f = open("/usr/local/bin/python3.10 /Users/byungwoyoon/Downloads/file1.txt","w")
# f.close()
# FileNotFoundError: [Errno 2] No such file or directory: '/usr/local/bin/python3.10 /Users/byungwoyoon/Downloads/file1.txt'

# f = open("./res/file.txt","w")
#         = "res/file.txt"
# FileNotFoundError: [Errno 2] No such file or directory: './res/file.txt'
# 현대 디렉터리 밑에 res라는 디렉터리가 없어서 에러
# f.close()

# 파일 경로
# 상대경로 - 현재 디렉터리를 기준으로 경로 생성 ex) ./res/file1.txt or res/file1.txt 같은의미
# ../res/f.txt - 현재 디렉터리보다 하나 위 디렉터리에서 res 디렉터리 찾고 그 안에 생성
# 절대경로 - 경로를 직접 정해주어 그 디렉토리에 생성


