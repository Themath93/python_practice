# 03_매개변수가 있는 생성자 함수
# __init__(self, 초기값파라미터1, 초기값파라미터2, ....)
# 기본값을 부여할 수도 있음
# self는 인수를 받지 않는 특수한 첫번째 파라미터이다.
class Person :
    # 객채 변수를 생성할 때 한번 호출 됨
    def __init__(self, name='Kate', age = 18,sex='F'): # self 현재 클래스(모듈) 자신을 가리킨다.
        # Person의 속성을 생성
        self.name = name # 초기값
        self.age = age
        self.sex = sex

class Rectalngle() :
    # 객채 변수를 생성할 때 한번 호출 됨
    def __init__(self,width, height):
        self.width = width
        self.height = height
    def calc(self):
        print("계산합니다.")

#### Person 인스턴스 생성
p1 = Person('성춘향',30) # sex는 기본값인 F 출력
p2 = Person('김철수',32,'M') # sex는 부여된 값인 M출력
p3 = Person()

print(p1.name,p1.age,p1.sex)
print(p2.name,p2.age,p2.sex)
print(p3.name,p3.age,p3.sex)

#### Rectangle 인스턴스 생성

r1 = Rectalngle(10,15)
r2 = Rectalngle(100,50)

print(r1.width,r1.height)
print(r2.width,r2.height)
# r1.calc()
