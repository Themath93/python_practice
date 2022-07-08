#  다음과 같은 함수를 포함하는 프로그램 작성
#  함수명 : order()
#  상품 가격과 주문 수량을 전달 받아서
#  주문액, 할인액, 지불액을 계산하여 반환
#  price, qty, amount, discount, total
#  할인액
#  주문액이 10만원 이상이면 10% 할인
#  주문액이 5만원 이상 10미만이면 5% 할인
#  주문액이 5만원 미만이면 할인 없음
def order() :
    price = eval(input("상품 가격 입력 : "))
    qty = eval(input("주문 수량 입력 : "))
    amount = price * qty
    if amount >= 100000 :
        discount = 10
    elif amount >= 50000 and amount < 100000 :
        discount = 5
    else :
        discount = 0
    dis_amount = int(amount * discount / 100)
    total = amount - dis_amount
    print("--------------------------------")
    print("주문액 : %d원" %amount)
    print("할인액 : %d원" %dis_amount)
    print("지불액 : %d원" %total)


order()

