#  다음의 함수를 포함하는 프로그램 작성
#  함수 이름 : get_area()
#  사각형의 가로길이와 세로길이를 입력 받아 면적을 구 하여 반환

def get_area() :
    width = eval(input("가로길이 입력 : "))
    length = eval(input("세로길이 입력 : "))
    return width*length

print("사각형의 면적 :",(get_area()))