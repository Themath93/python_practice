# for문
# 정해진 횟수만큼 반복

# for 변수 in 리스트 또는 범위:
    #반복문장
    #반복문장

for name in ["홍길동","이몽룡","성춘향","변학도"] :
    print(name)

for i in range(0,9): # 0~9
    print(i)

# 줄바꿈하지 않고 출력 print(변수, end=' ') end= '문자열' >> 줄바꿈 없이 출력할 때 각 리스트 값의 사이에 넣어줄 문자열
print("======================================")
for x in range(0, 9) :
    print(x, end=' ')
print("")
print("========================================")

#range() 함수
# range(10) : 0 ~ 9 까지의 정 (10개 /시작은 0)

# range(start, stop)
    # start에서 stop-1까의 정수
    # range(0,10) : 0 ~ 9 까지의 정수

# for i in range(10) :
#     print(i, end = ' ')
#
# for i in range(10,0,-1) : #거꾸로 출력 step -1 이 디폴트값
#     print(i,end=' ')
#     print("")


# # 누적 변수 sumX가 반드시 초기화 되어있어야한다.
# sumX = 0
# for x in range(10) :
#     print(x)
#     sumX = sumX + x
# print("sum =", sumX)
#
# scores = [60, 100, 70, 70, 55]
# num = 0
#
# for score in scores :
#     num = num + 1
#     if score >= 60:
#         result = "합격"
#     else:
#         result = "불합격"
#     print("%d번 %d점 %s " % (num,score,result))
# for score in scores :
#     num = num + score
# print("평균점수 : %d" % (num/5))

# 다중 for 문
from random import randint

for y in range(10):
    for x in range(10):
        print(randint(1,9), end=" ")

    print()

