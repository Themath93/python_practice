# 데이터형변환

# 정수를 실수로 문자열로
num = 10
print(num)
print(float(num))
print(str(num))
print("\n")

# 실수를 정수로 문자열로
pi = 3.141592
print(pi) # 실수
print(int(pi)) # 정수 반올림없이 소수점 삭제
print(str(pi)) # 문자열
print("\n")

# 문자열을 정수 및 실수로
print("\n)")
str1 = "100.1234"
print(str1)
# print(int(str1)) #실수형 문자열을 바로 int로 변환 불가
print(float(str1))
print(int(float(str1))) # 실수형 문자열을 정수로 변환시 실수로 바꿔준 후 그걸 다시 정수로 변환

#형변환 예제
age = 23

print("나는 현재 " + str(age) + "살 입니다.") # 문자열과 정수 실수 타입은 + 가 불가능하다.
print("나는 현재", age, "살 입니다.") # 문자열과 정수 및 실수변수를 같이 쓰려면 , comma로 이어준다.



