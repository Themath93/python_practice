#  가위 바위 보 게임 함수 작성
#  함수명 : gbb_game()
#  랜덤으로 COM 숫자를 생성해서
#  전달받은 YOU 숫자와 비교하여
#  결과 출력
from random import randint
def gbb_game():
    com = randint(1,3)
    you = int(input("YOU 입력 (1:가위, 2:바위, 3:보) : "))
    if com == you :
        print("비겼습니다.")
        print("COM : %d" %com)
    elif (you == 1 and com == 3) or (you == 3 and com == 2) or (you == 2 and com == 1):
        print("당신이 이겼습니다.")
        print("COM : %d" % com)
    else:
        print("당신이 졌습니다.")
        print("COM : %d" % com)

gbb_game()
