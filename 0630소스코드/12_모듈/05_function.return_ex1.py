# 사각형의 면적구하기

def get_area():
    width = eval(input("가로 길이 입력 : "))
    height = eval(input("세로 길이 입력 : "))
    area = width * height
    return area


# 호출 테스트
rect_area = get_area() #함수 호출 후 반한된 결과값이 호출한 코드 자리로 전달
# 위에 함수를 호출해야 위 정의된 함수가 실행된다. 13번이 이 프로그램의 시작점
print("사각형의 면적 : %d" % rect_area)
# print("사각형의 면적 : %d" % get_area())
