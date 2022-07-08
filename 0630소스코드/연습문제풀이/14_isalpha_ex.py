# 사용자로부터 문장을 입력받아, 문자/숫자/공백/기타 의 개수를 세는 프로그램

string = input("문장을 입력하세요 : ")

# 문자열은 집합형태기 때문에 for문의 반복 요소로 사용가능
# 한글자씩 순회하면서 문자/숫자/공백/기타 여부를 판단해서 계수함

# 각 요소들의 갯수를 저장할 변수가 필요(누적변수)
alphas = digits = spaces = others = 0

for s in string :
    # 판단
    if s.isalpha() :
        alphas += 1 # s가 문자인 경우
    elif s.isdigit() :
        digits += 1 # s가 숫자인 경우
    elif s.isspace() :
        spaces += 1
    else :
        others += 1

print("문자 : %d개" % alphas)
print("숫자 : %d개 " % digits)
print("스페이스 : %d개" %spaces)
print("기타 : %d개" % others)

