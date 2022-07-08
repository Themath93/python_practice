# while문
# 정해진 조건에 따라 반복 수행
# 조건식을 먼저 확인한 후 참이면 문장 반복 수행

# i = 1 #초기값
# while i <= 10: #조건
#     print(i,end=' ')
#     i = i + 1

# 1부터 100까지 모든 3의 배수의 합을 계산하여 출력 while 문사용
# num = 1
# sum = 0
# while num <= 100:
#     if num % 3 == 0 :
#         sum = sum + num
#     num += 1
#
# print(sum)
# x = 0
# for i in range(33): # 0~32
#     i = 3 * i + 3
#     x = x + i
# print("1부터 100 사이의 모든 3의 배수의 합은 %d입니다." %x)

# 무한반복문
 # 조건이 무조건 참인 경우 계속 반복
 # 반복문을 종료하기 위해 break문 필요
#
# while True:
#     print("반복 수행 되는 문장 입니다.")
#     answer = input("종료 하려면 x 입력 : ")
#     if answer == 'x':
#         break
# print("종료했습니다.")

# 노래방기계
# amount = 10000
# print("노래 1곡에 2000원입니다.")
# while True:
#     songnum = input("노래번호를 입력 해주세요.('x'입력시종료) : ")
#     if songnum != "x" :
#         amount = amount - 2000
#     restsong = amount / 2000
#     print("%d곡 남았습니다." %restsong)
#     if amount < 2000 :
#         print("잔액이 부족합니다.")
#         break
# print("프로그램을 종료합니다.")

song = 2000
money = 10000
count = 0

while money != 0:
    count += 1
    money = money - song
    print("노래를 %d 곡 불렀습니다." % count)
    if money == 0:
        print("잔액이 부족합니다.")
        break
    else:
        print("현재 %d 원 남았습니다." %money)
print("프로그램을 종료합니다.")