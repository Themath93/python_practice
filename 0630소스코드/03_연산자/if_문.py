# password = eval(input("비밀번호를 입력해주세요 : "))

# if password == 1234 :
#     print("비밀번호가 일치합니다.")
# else :
#     print("비밀번호가 일치하지 않습니다.")

# if password == 1234 :
#     print("비밀번호가 일치합니다.")
# else :
#     print("비밀번호가 일치하지 않습니다.")

#
# num = eval(input("숫자 입력 : "))
#
# if num > 0 :
#     print("양수")
# elif num < 0 :
#     print("음수")
# else
#     print(0)

# from random import randint
# n1 = randint(1,100)
# n2 = randint(1, 5)
#
# print(n1,n2)

apple_quality = input("사과 상태 입력 : ")

if apple_quality == "신선":
    apple_price = int(input("사과 가격 입력 : "))
    if apple_price <=1000 :
        print("10개를 산다.")
        print("Total Price : " + str(apple_price*10))
    else :
        print("5개를 산다.")
        print("Total Price : " + str(apple_price * 5))
else:
    print("사과를 사지않는다.")

