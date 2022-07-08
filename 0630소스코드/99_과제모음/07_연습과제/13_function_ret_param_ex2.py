# 다음의 함수를 포함하는 프로그램 작성
#  함수 이름 : get_interest()
#  예금액과 이자율을 전달받아서 이자액을 구하여 반환
#  deposit, int_rate, interest

def get_interest() :
    dep = eval(input("예금액 입력 : "))
    rate = eval(input("이자율 입력(%) : "))
    interest = dep * rate / 100
    print("이자액 : " + str(format(int(interest), ',d'))+"원")
    return dep * rate / 100

get_interest()

