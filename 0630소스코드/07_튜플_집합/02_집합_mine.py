s = {1,2,3,4,5}
f = {3}
print(type(s))
print(len(s))
s.remove(3) # 요소 중 3의 값을 지닌 값을 제거 중복은 없으니 한 번에 해당 요소는 사라짐
print(s)
print(s | f)
print("-----------------------------------------")
a ={1,2,3}
b ={3,4,5}
# 합집합
c = a | b
print("합집합 : ",c)
print("차집합 : ",a-b)
print("차집합 : ",b-a)
print("교집합 : ",a&b)