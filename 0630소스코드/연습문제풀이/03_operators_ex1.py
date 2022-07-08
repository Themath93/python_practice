# 현금이 5,000원이 있고, 사탕 가격이 120원인 경우
# 최대한 살 수 있는 사탕의 개수와 나머지 돈은 얼마 인가?

money = 5000
candyprice = 120

# 최대한 살 수 있는 사탕 수
candies = money // candyprice

# 최대한 사탕을 구입 하고 남은 돈
change = money % candyprice

print("%d개, 남은 돈 : %d원" % (candies, change) )
