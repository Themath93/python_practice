a = "Python"
pi = 3.141592

print("{0:.2f}".format(pi))
print("{0:10.2f}".format(pi))

total = 286
average = total / 3

print("총점: {0}, 평균:{1:.1f}".format(total, average))

print("{0:<10}".format(a))
print("{0:>10}".format(a))
print("{0:^10}".format(a))
print("{0:-^10}".format(a))
print("{0:-^100}".format(""))

name = "홍길동"
age = 23

print("이름 : {0}, 나이 : {1}".format(name,age))
print("{name}은 {age}살입니다.".format(name="이몽룡",age=23))

from datetime import date, datetime, timedelta

today = date.today()
year = today.year
month = today.month
day = today.day

print("오늘 날짜 : {0}".format(today))
print("연도 : {0}년".format(year))
print("월 : {0}월".format(month))
print("일 : {0}년".format(day))



current_time = datetime.now().time()
hour = current_time.hour
minute = current_time.minute
second = current_time.second
microsecond = current_time.microsecond

print("현재 시간 : {0}".format(current_time))
print("시 : {0}시".format(hour))
print("분 : {0}분".format(minute))
print("초 : {0}초".format(second))
print("마이크로초 : {0}마이크로초".format(microsecond))
print()
print("오늘 : {0}".format(today))
print("어제 : {0}".format(today + timedelta(days=-1)))
print("내일 : {0}".format(today + timedelta(days=1)))
print("일주일 전 : {0}".format(today + timedelta(days=-7)))
print("일주일 후 : {0}".format(today + timedelta(days=7)))
print("한달 후 : {0}".format(today + timedelta(days=30)))