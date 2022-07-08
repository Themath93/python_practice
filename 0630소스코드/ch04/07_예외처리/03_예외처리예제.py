# 여러 개의 예외 처리문이 있으면 : 첫번째 오류에 대해서만 오류처리가 가능하다.


# a = [1,2,3]

# try :
#     print(10/0) # 오류에 대해 예외처리하고
#     print(a[4]) # 처리되지 않는다.
# except ZeroDivisionError as e :
#     print("0으로 나눌 수 없습니다.")
# except IndexError as e :
#     print("인덱스 범위를 벗어났습니다.")


# try :
#     print(10/2)
#     print(a[4]) # 처리되지 않는다.
# except ZeroDivisionError as e :
#     print("0으로 나눌 수 없습니다.")
# except IndexError as e :
#     print("인덱스 범위를 벗어났습니다.") #list index out of range

#여러개의 예외를 한번에 처리
# a = [1,2,3]
# try :
#     # print(10/0)
#     print(10/2)
#     print(a[4])
# except (ZeroDivisionError,IndexError) as e :
#     print("오류가 발생 했습니다.",e)

# else 구문없이 위 구문만으로 여러개의 오류를 한번에 예외처리 불가


# 오류 발생시 아무것도 하지 않고 넘기기
# 파일 읽어오기를 수행할 때 파일이 없어 오류가 나면 pass
# 파일이 있으면 읽고 출력

try :
    f=open("exception.txt",'r')
except FileNotFoundError:
    pass
else :
    data = f.read()
    print(data)
    f.close()
finally:
    print("종료")