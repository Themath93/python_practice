# 매개변수
 # 함수로 전달되는 값을 받는 변수
 # 함수정의할 때 사용 되는 변수
 # 매개변수는 반드시 인수가 전달 되어야 함



# 인수(argument)
 # 함수에게 실제로 전달되는 값
# 함수이름 : get_interest()
# 예금액과 이자율을 전달받아서 이자액을 구하여 반환
# deposit, int_rate, interest : 사용 변수명

def get_interest(deposit,int_rate):
    interest = deposit * int_rate / 100
    return int(interest)
print(get_interest(100000,2.5))

deposit = int(input("예금액 입력"))
int_rate = float(float)
interest = format(get_interest(deposit,int_rate)), ",")
