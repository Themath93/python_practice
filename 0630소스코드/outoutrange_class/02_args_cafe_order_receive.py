# 1.커피 종류 선택
# 2.사이즈 선택
# 3.HOT or ICE 선택
# 4.stay or go

def order_coffee(coffee,*options) :
    print(coffee + ", 옵션: ", end=' ')

    for opt in options :
        print(opt, end= ', ')
    print()

order_coffee("아메리카노",'Tall','HOT','시럽추가','stay')