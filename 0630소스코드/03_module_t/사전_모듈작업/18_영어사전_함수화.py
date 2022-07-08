# 영어사전 프로그램 - 모듈화
# 사전 생성 모듈 : 단어를 사전에 등록하는 기능
# dict_const.py
# 1. 단어를 전달 받아 사전에 단어를 등록 : input_dict(eng)
# 2. 등록전 단어 필터링 : const_dict()

# 사전 검색 모듈 : 등록된 사전을 이용해 검색 기능
# dict_search.py
# 1. 단어를 전달받아 뜻을 검색 후 출력하는 함수 : dict_search(eng)
# 2. 검색하려는 단어를 입력받아 사전에 있는 지 필터링 : search()
# 사전 사용 메뉴 프로그램

# 공용 사용 변수 모듈
# dict_var.py

# 필요 모듈 import
from dict.dict_const import *
from dict.dict_search import *
from dict.dict_inout import *



# 메뉴 : 사전 프로그램은 사용자가 종료를 선택하면 완전 종료

while True :
    print("=============메 뉴===============")
    print("1. 사전 등록 : ")
    print('2. 사전 검색 : ')
    print("3. 종료 : ")

    sel = input("사용할 메뉴를 선택 하세요. 1/2/3/ : ")

    if sel == '1' :
        print("사전에 단어를 등록합니다. 원하는 단어 수 만큼 등록이 가능합니다.")
        const_dict() # 사전 등록 함수
        # print(ek_dic)
    elif sel == '2' :
        print("단어 1개에 대하여 검색합니다. ")
        search() # 사전 검색 전 필터링 함수
    else :
        print("사전 프로그램을 종료 합니다. ")
        break


