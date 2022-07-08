#input
# 키보드로부터 입력 받은 값 반환
# 변수 = input()
# 이때 입력된 값의 자료형 문자열

# 변수 = input("프롬프트 문자열")
# 입력 받기 전에 프롬프트 문자열 출력
#
# name = input("이름 : ")
# age = input("나이 : ")
#
# print("이름: " + name + "\n" + "나이: " + age )
#
# # input() 함수로 반환되는 값은 반드시 문자열!
#
# x = input("숫자1 입력 : ")
# y = input("숫자2 입력 : ")
# sum = x + y
# print(sum) #문자열로 출력
# sum = int(x) + int(y)
# print(sum)

#숫자로 변환

x = eval(input("숫자1 입력 : "))
y = eval(input("숫자2 입력 : "))

sum = x + y
print(sum)
print(type(sum))

# int() vs eval() int함수는 정수만 변환 가능하지만 eval함수는 정수 실수 모두 변환가능

