class Person :
    # 객채 변수를 생성할 때 한번 호출 됨
    def __init__(self, name='Kate', age = 18,sex='F'): # self 현재 클래스(모듈) 자신을 가리킨다.
        print('self : ',self)
        # Person의 속성을 생성
        self.name = name # 초기값
        self.age = age
        self.sex = sex

    def sleep(self): # 파라미터가 1개 있는 method, 단, 첫번째 파라미터는 클래스의 참조값 포인터를 전달받는다.
        print('self : ', self)
        print(self.name, '은 잠을 잡니다.')

class Rectalngle() :
    # 객채 변수를 생성할 때 한번 호출 됨
    def __init__(self,width, height):
        print('self : ',self)
        self.width = width
        self.height = height

    def calcArea(self): # 파라미터가 1개 있는 method, 단, 첫번째 파라미터는 클래스의 참조값 포인터를 전달받는다.
        area = self.width * self.height
        return area

##############################
# class 객체 생성 및 사용

# a = Person('Aaron',20,'M')
# b = Person('Bob',30)
# 복사된 클래스의 주소를
# print(a) # a 는 객체 인스턴스
# print(b)

# 객체 인스턴스 전용 주소가 아래로 계속전달된다.
# a.sleep()
# b.sleep()

# Rectangle 클래스 사용
r_a = Rectalngle(10,5)
r_b = Rectalngle(3.5,2.1)

print("면적 r_a : ",r_a.calcArea())
print("면적 r_b : ",r_b.calcArea())