# # 1. 1에서20수중에서3의배수만출력
#
# for i in range(6) :
#     i = 3*i +3
#     print(i, end=' ')

# #2. 등차수열의 합
# n1 = eval(input("숫자1 입력 : "))
# n2 = eval(input("숫자2 입력 : "))
# n3 =0
# for i in range(n1-1,n2):
#     i = i +1
#     n3 = n3 + i
# print("%d부터 %d까지의 합 : %d" %(n1,n2,n3))

# # 3. 카운트다운프로그램
# n1 = eval(input(("시작 숫자 입력하시오 : ")))
# for i in range(n1,0,-1):
#     print(i,end=' ')
# print("발사")

# # 4. 숫자10개를입력받아서양,음,0의개수출력
#
# from random import randint
# plus = 0
# minus = 0
# zero = 0
# for i in range(1,11):
#     d = randint(-10,10)
#     print("숫자%d입력 : %d" %(i,d))
#
#     if d > 0:
#         plus = plus + 1
#     elif d < 0:
#         minus = minus + 1
#     else:
#         zero = zero + 1
# print("--------------------------------------")
# print("양의 개수 : %d" %plus)
# print("음의 개수 : %d" %minus)
# print("0의 개수 : %d" %zero)
#


# # 5. 명단확인
#
# names = ["홍길동", "이몽룡", "성춘향", "변학도"]
# check = input("이름 입력 : ")
# for name in names:
#     if check == name:
#         print("명단에 있습니다.")
#         check = input("이름 입력 : ")
#     else:
#         continue
# print("명단에 없습니다.")

# 6. 다중 for문
j=0
for i in range(1,4):
    print()
    for j in range(j,j+4):
        j += 1
        print(j,end=' ')


