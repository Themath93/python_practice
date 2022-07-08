#  다음의 함수를 포함하는 프로그램 작성
#  함수명 : order()
#  상품가격, 주문수량을 입력 받아서, 주문액을 구하여 반환

def order() :
    price = eval(input("상품가격 입력 : "))
    qty = eval(input("주문수량 입력 : "))
    print("-----------------")
    print("상품가격 : %d원" %price)
    print("주문수량 : %d개" %qty)
    print("주문액 : %d원" %(price*qty))


order()
