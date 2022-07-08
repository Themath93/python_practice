#에러 종류와 상관없

# try :
#     # print(10/0) # 오류발생
#     print("나이"+23)
# except :
#     print('오류발생') # 정상종료

# 최상위 에러인 Exception 적어도 됨
# 에러종류 명시
# try :
#     print(10/0) # 오류발생
#     print("나이"+23) #위에서 에러가 발생하여 except로 가버려 실행되지 않음
# except ZeroDivisionError :
#     print('오류발생') # 정상종료


# 에러 저오류 명시 메시지 변수 사용 가능

try :
    print(10/0)
except ZeroDivisionError as e:
    print("0으로 나눌 수 없습니다.")

# 오류를 에러로 처리하지핞고 그냥 처리
print(3+5)