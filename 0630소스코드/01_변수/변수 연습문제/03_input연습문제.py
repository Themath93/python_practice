# # 연습문제 1
# kor = eval(input("국어 점수 입력: "))
# eng = eval(input("영어 점수 입력: "))
# math = eval(input("수학 점수 입력: "))
#
# sum = kor + eng + math
# average = sum / 3
#
# print("총점: %d, 평균: %f" %(sum,average))

# # 연습문제 2 BMI 계산
#
# weight = eval(input("몸무게(kg) : "))
# height = eval(input("키(m) : "))
# bmi = weight / height ** 2
#
# print("당신의 BMI %.2f" %bmi)

# 연습문제 3 이자계산

money = eval(input("예금액 입력 : "))
interest = eval(input("이자율 입력(%) : "))
profit =  money * interest / 100
totalmoney = money + profit
print("-------------------------")
print("예금액 : %d" %money, "원")
print("이자율 : %.1f" %interest, "%")
print("예금이자 : %d" %profit, "원")
print("잔액 : %d" %totalmoney, "원")
print("-------------------------")
print("예금액 :",f'{money:,}', "원")
print("이자율 :",f'{interest:,}', "%")
print("예금이자 :",f'{int(profit):,}', "원")
print("잔액:",f'{int(totalmoney):,}', "원")



