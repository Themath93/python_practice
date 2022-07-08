# 생성자 함수
# 클래스라는 개념을 만들어 낼 때 반드시 필요하다라고 약속된 특수 함수

# 개발자가 안만들면 번역기가 무조건 정의함

# 파이썬에서 생성자 함수를 만들기 위해서는
# __init__(self) 라고 정의하기로 약속 했다.

class Person :
    # 객채 변수를 생성할 때 한번 호출 됨
    def __init__(self): # self 현재 클래스(모듈) 자신을 가리킨다.
        # print(self, 'is generated')
        # Person의 속성을 생성
        self.name = 'kate' # 초기값
        self.age = 10
    def __str__(self):
        return '{},{}'.format(self.name,self.age)

p1 = Person()
print(p1)
class Rectalngle() :
    # 객채 변수를 생성할 때 한번 호출 됨
    def __init__(self):
        print(self, 'is generated')
        self.width = 1
        self.height = 1

# # 생성자 함수를 호출 하는 방법 : 객채변수를 생성
# p1 = Person() # p1 객채변수 생성자 함수 호출
# #p1이라는 객채변수 생성자 함수하나 호출한 번하여 2개의 변수생성을 했다.
# p2 = Person() # p2 객체변수 생성자 함수 호출
#
# print(p1.name) # p1이 사용할 수 있는 변수 name 을 생성했음
# print(p2.name) # p2만 사용할 수 있는 변수 name 을 생성했음
#
# p1.name = 'Hong'
# p2.name = 'Lee'
# print(p1.name)
# print(p2.name)
#
# p2.age = 36
# p1.age = 25
# print(p1.age)
# print(p2.age)
#
# r1 = Rectalngle() # r1 생성자 함수가 호출됨
# r2 = Rectalngle()
#
# print(r1.width,r1.height,"디폴트값출력")
# r1.width = 10; r1.height = 15
# print(r1.width,r1.height,"생성자 함수 호출로 생성된 두개의 변수 값을 바꿔준 값으로 출력")
#
# print(r2.width,r2.height,"디폴트값출력")
# r2.width = 100; r2.height =50
# print(r2.width,r2.height)
#
#
# #test
# l1 = list((1,2,3))

