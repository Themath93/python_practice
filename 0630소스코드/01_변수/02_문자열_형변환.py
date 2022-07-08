name = "홍길동"
age = 23

print("나의 이름은 " + name + "이며 나이는 "+ str(age) +"살 입니다.")

name, no, year, grade, average = "홍길동", 2016001, 4, 'A', 93.5

print("성명 : %s" % name)
print("학번 : %s" % no)
print("학년 : %d" % year)
print("등급 : %c" % grade)
print("평균 : %.1f" % average) # %.numf 여기서 .num은 소수점 몇번째 자리 까지 출력할 것인지 나타낸다.

print(type("학년 : %d" % year))
print(type(year))

print("=======================================")
#화씨를 섭씨로 변경
ftemp = 90
ctemp = (ftemp - 32) * 5 / 9
gap_temp = ctemp - ftemp
print(ctemp)

#소숫점 둘째 자리까지만

print("%.2f" %ctemp)
print("%.4f" % gap_temp)
print("%.2f, %d" %(ctemp , ftemp))

