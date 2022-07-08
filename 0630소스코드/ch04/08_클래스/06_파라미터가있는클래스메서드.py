class Rectalngle() :
    # 객채 변수를 생성할 때 한번 호출 됨
    def __init__(self,width=1, height=1):
        print('self : ',self)
        self.width = width
        self.height = height
    # instance method - 객체(instance)를 이용해서 호출
    def calcArea(self,width=1,height=1): # 파라미터가 1개 있는 method, 단, 첫번째 파라미터는 클래스의 참조값 포인터를 전달받는다.
        if width > 0 and height > 0 :
            area = width * height
        else:
            area = self.width * self.height
        return area

r_1 = Rectalngle()

print('r_1의 면적 : ',r_1.calcArea(5,3))
