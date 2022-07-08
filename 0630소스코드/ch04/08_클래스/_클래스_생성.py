# 클래스 정의하기
# 인스턴스(클래스객체변수)를 생성하기 위해서는 모체가 되는 클래스를 정의 해야됨
# claas 클래스명 :
#   클래스 생성자
#   클래스 속성(변수,특성)
#   클래스 메서드(기능, 함수)

# person 클래스 정의
# 빈클래스로 정의
class person :
    pass # 빈클래스 정의 완료!

# Rectangle 클래스 정의
# 속성과 메서드를 포함
class Rectangle :
    count = 0 # 클래스 속성

    def __init__(self): # 클래스 생성자
        # self는 내부에서 알아서 만들어주는 매개변수라 이경우 생성자 매개변수를 따로 적어줄 필요는 없다.
        Rectangle.count += 1

    def print_count(self): # 클래스 메서드
        print(self.count)

# print_count() # 클래스 내부에 있는 함수기 때문에 객체 인스턴스 생성 후 사용 가능하다.

# 클래스 객체 인스턴스(객체변수) 생성
# 변수명 = 클래스명([생성자매개변수])
rect1 = Rectangle()

# 객체변수 rect1을 이용해 메서드 print_count()
rect1.print_count()
rect1.count

# Rectangle() 클래스는 복사를 통해 여러개의  인스턴스를 만들 수 있다.
rect2 = Rectangle()
rect3 = Rectangle()
###### 파이썬 내부 클래스 사용 예제
### 형변환 함수
a = '123'
# int는 클래스 이름
# 아래코드는 int 클래스 생성자 함수를 호출
int(a)
int_a = int(a) # int_a는 int클래스의 인스턴스(객체변수)

b = 123
str_b = str(b) # str_b는 str클래스의 인스턴스(객채변수)
# str클래스의 생성자 함수를 호출한

str_b.replace('1','b')
print(str_b)