

def show_list(my_list) :
    print('함수 내부에서 출력1 : ', my_list)
    my_list[0]= 10 # 리스트 부분변경
    print("함수 내부 출력2, : ", my_list)
    print("함수 내부 출력, id : ", id(my_list))
    my_list = [100,200,300]
    print("함수 내부에서 출력3 : ", my_list)
    print("함수 내부 출력, id :")


    my_list = [1,2,3,4]
