
# 파이썬 내장함수
# 파이썬에 이미 만들어져 있어 내장되어 있는 함수들 , 별도의 모듈이 필요하지 않다.
# 형식에 맞춰 함수 이름만 호출해서 사용
# ex) print(), input(), type()

# abs() 함수
# abs(x) : x의 절대값 반환
print(abs(-10))

# all() 함수
# all(iterable) : 모든 요소가 참이면 True 거짓이면 False 반환
# 0이 하나라도 있으면 False 반환


print(enumerate(['s','d','f']))

for i, name in enumerate(['s','d','f'],start=1):
    print(i,name)

def positive(x) :
    return x > 0

print(list(filter(positive,[0,-1,5,-7,10])))

def evne_n(x):
    if x % 2 == 0:
        return x

list_n = [1,2,3,4,5,6,7,8,9,10]
flt_list = list(filter(evne_n,list_n))
print(list(filter(evne_n,list_n)))

sumX = 0
for i in flt_list:
    sumX = sumX + i
print(sumX)

print(type(hex(12123)))

print("\n--- map ---")
# map(function, iterable)
# iterable 각 요소를 함수에 전달해서 수행된 결과를 반환

def increase(x):
    return x+1
list_i = [1,2,3,4,5,6,7,8,9,10]
x=0


# open(filenamem [mode]) : mode 형식으로 파일 열기
# mode(읽기 방법) : 생략시 읽기 전용 모드(r)가 기본
# w, r, a, b 쓰기, 읽기, 원본내용뒤에 추가, 이미지처리모드
# 현재 디렉터리에 'my_file,txt'를 쓰기 모드로 생성
file_write = open('my_file.txt', 'w')
# file_write변수는 외부 파일인 my_file.txt 를 사용할 수 있는 핸들러가 저장됨

#pow()는 제곱한 결과값을 반환해주는 함수
print(pow(10,3))

# round() 실수를 반올림하여 반환
#
# round(number, ndigits)

print(round(3.141592,3))


# enmurate, lamb