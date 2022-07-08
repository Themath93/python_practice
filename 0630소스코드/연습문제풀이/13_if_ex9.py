print("******************상품 정보*********************")
print("1 노트북 : 1,200,000 원")
print("2 디지털카메라 : 400,000 원")
print("***********************************************")

# 상품번호 입력
num = int(input("상품 번호 입력 : "))

# 상품번호 오류 확인
if num != 1 and num != 2 : # 상품번호 잘 못 입력한 경우
    print("\n잘못 입력하였습니다. 종료합니다.")
else : # 상품번호 제대로 입력한 경우
    qty = int(input("주문 수량 입력 : "))

    # 입력번호에 따라 상품명과 가격 결정
    if num == 1 :
        product = "노트북"
        price = 1200000
    else :
        product ="디지털카메라"
        price = 400000

    # 주문액 계산
    amount = qty * price

    # 할인액 계산
    if amount >= 1000000 and amount < 5000000 :
        discount = int(amount * 0.1)
        dicslevel = 10
    elif amount >= 5000000 :
        discount = int(amount * 0.2)
        dicslevel = 20
    elif amount > 500000 :
        discount = int(amount * 0.05)
        dicslevel = 5
    else :
        discount = 0
        dicslevel = 0

    # 지불액 계산
    total = amount - discount

    # 주문 정보 출력
    print("\n******************주문 정보*********************")
    print("상품명    : \t", product)
    print("가  격   : \t", format(price, ','), "원")
    print("주문 수량 : \t", qty)
    print("주문액    : \t", format(amount, ','), "원")
    print("할인수준  : \t", format(dicslevel, ','),"%")
    print("할인액   : \t", format(discount, ','), "원")
    print("총지불액  : \t", format(total, ','), "원")






# if num == 1 or num == 2 : # 상품번호 제대로 입력한 경우
#     qty = int(input("주문 수량 입력 : "))
# else : # 상품번호 잘 못 입력한 경우
#     print("\n잘못 입력하였습니다. 종료합니다.")