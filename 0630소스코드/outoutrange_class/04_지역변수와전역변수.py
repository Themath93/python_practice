a = 1 #함수 밖에서 정의된 전역변수 a

def show() :
    c = a+b
    print(a)
    print(b)
    print(c)

def add():
    print(a)
    print(b)

b = 2

show()
add()
print(a)
print(b)