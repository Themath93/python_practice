# 부모 클래스
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self, food):
        print('{}은 {}를 먹습니다.'.format(self.name, food))

    def sleep(self, minute):
        print('{}은 {}분동안 잡니다.'.format(self.name, minute))

    def work(self, minute):
        print('{}은 {}분동안 일합니다.'.format(self.name, minute))

# child 클래스인 Student와 Employee를 생성(Person 클래스 상속)
# 생성자 함수는 다시 선언해서 각 클래스 속석을 재구성

# Person클래스 상속을 받아 Student 클래스 생성
# 상속 형식
# class 자식클래스명(부모클래스명) :
class Student(Person) :
    # Student속성 name과 age는 재구성
    # 생성자 함수
    def __init__(self,name,age):
        self.name = name
        self.age = age
# Person클래스 상속을 받아 Employee 클래스 생성
class Employee(Person) :
    # Employee속성 name과 age는 재구성
    # 생성자 함수
    def __init__(self,name,age):
        self.name = name
        self.age = age

bob = Employee('Bob',25)
lee = Student('Lee',19)

bob.sleep(30) #Person 부모클래스의 sleep()메서드를 사용할 수 있따.
bob.eat('Rice')
lee.work(50) #Person 부모클래스의 word()메서드 이용 가능
lee.sleep(30)
