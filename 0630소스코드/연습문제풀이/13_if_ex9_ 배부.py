print("******************상품 정보*********************")
print("1 노트북 : 1,200,000 원")
print("2 디지털카메라 : 400,000 원")
print("***********************************************")

product = "노트북"
price = 1200000
qty = 1
amount = 1200000
discount = 120000
total = amount - discount

print("\n******************주문 정보*********************")
print("상품명 : \t",product)
print("가  격 : \t", format(price,','),"원")
print("주문 수량 : \t",qty)
print("주문액 : \t", format(amount,','),"원")
print("할인액 : \t", format(discount,','),"원")
print("총지불액 : \t", format(total,','),"원")