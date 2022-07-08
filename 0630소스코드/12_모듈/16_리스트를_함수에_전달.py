# 리스트가 함수에 인수로 전달 시 알아야 할 사항
# 함수 정의

def show_list(my_list) : # 매개변수 my_list
    print("함수내부 출력1",my_list) # 지역변수 my_list [1, 2, 3, 4] 출력
    print("매개변수 my_list의 id : ", id(my_list))
    my_list[0] = 50 #my_list의 첫번째 요소 변경
    print("함수내부 출력2",my_list)

# 호출 테스트
my_list = [1,2,3,4] # 리스트 생성
print("출력1",my_list)
show_list(my_list) # 리스트를 인수로 전달
print("출력2",my_list) # 전역변수 my_list [1, 2, 3, 4] 출력
# 함수 내부에서 변경시킨 값이 그대로 함수 외부에도 반영
print("전역변수 my_list의 id : ", id(my_list))

# [1, 2, 3, 4]
# 매개변수 my_list의 id :  4347536576
# [1, 2, 3, 4]
# 전역변수 my_list의 id :  4347536576
# 주소 동일 같은 리스트
# 함수 내에서 변경시 함수 외부에서도 영향을 받는다.
