# 스태틱/클래스 메서드 : @staticmethod / @classmethod
# 클래스명.메서드로 접근

class Math :
    @staticmethod
    def add(a,b):
        return a+b

    @staticmethod
    def multiply(a,b):
        return a*b

# 클래식 메서드로 사용 객체 인스턴스 생성 x
print("클래식메서드로 접근 : ", Math.add(10,20))
print("클래식메서드로 접근 : ", Math.multiply(10,20))

# 일반 객체 메서드로 접근
m_o = Math() #객체 인스턴스 생성
print("객체메서드로 접근 : ", Math.add(10,20))
print("객체메서드로 접근 : ", Math.multiply(10,20))