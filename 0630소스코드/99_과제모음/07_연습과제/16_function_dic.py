# 다음과 같은 함수를 포함하는 프로그램 작성
#  함수명 : show_info()
#  이름, 학년, 나이, 연락처를 전달 받아서 딕셔너리로 만들어 출력

def show_info(name,year,age,phone) :
    # name = input("이름 입력 : ")
    # year = input("학년 입력 : ")
    # age = input("나이 입력 : ")
    # phone = input("연락처 입력('-'표시) : ")
    dict_school = {'name':name, 'year':year, 'age':age, 'phone':phone}
    print(dict_school)

show_info('홍길동',4,23,'010-1234-1234')

