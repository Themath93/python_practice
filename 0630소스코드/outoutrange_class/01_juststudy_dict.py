# def get_info() :
#     name = input("이름 입력 : ")
#     age = input("나이 입력 : ")
#
#     # key:value 딕셔너리 만들기
#     student ={'name': name, 'age': age}
#
#     return student
#
# student_info = get_info()
# print(student_info)
# def show():
#     print("안녕하세요.")
#     return 1
# print(show())

def show_info(info) :
    print(info) #딕셔너리 전체 출력
    # key가 name, value가 kim
    print("이름 : "+info["name"])
    # keyrk phone, value가 010-1234-1234
    print("연락처 : " + info["phone"])

info_list = {'name': 'kim','age': 23, 'phone': '010-1234-1234'}
show_info(info_list)
