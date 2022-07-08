# 영어사전 프로그램 - 클래스화
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
from dict_class import *
# 새로운 사전 생성여부 확인
con_sel = int(input("새로운 사전을 생성 하려면 1을 기존 사전을 사용하려면 2를 입력하세요."))

if con_sel != 1 and con_sel != 2 :
    pass
else :
    print("새로 사전을 구성하시는 분은 새 사전의 사전명을 입력하세요.")
    print("기존 사전 사용하시는 분은 기존 사전명이 필요합니다.")
    d_name = input('사전명을 입력하세요 : ')

    eng = Dict_Const(d_name) #d_name 은 file_name

    if con_sel == 2 : # 기존 사전 사용 - 사전 준비
        eng.load_dict()

    # 사전 사용 메뉴 프로그램
    ################################################
    # 메뉴 : 사전 프로그램은 사용자가 종료를 선택하면 완전 종료

    while True :
        print("=============메 뉴===============")
        print("1. 사전 등록 : ")
        print('2. 사전 검색 : ')
        print("3. 종료 : ")

        sel = input("사용할 메뉴를 선택 하세요. 1/2/3/ : ")

        if sel == '1' :
            print("사전에 단어를 등록합니다. 원하는 단어 수 만큼 등록이 가능합니다.")
            eng.const_dict() # 사전 등록 함수
            # print(ek_dic)
        elif sel == '2' :
            print("단어 1개에 대하여 검색합니다. ")
            eng.search() # 사전 검색 전 필터링 함수
        else :
            print("사전 프로그램을 종료 합니다. ")
            eng.save_dict() # 사전을 파일로 저장하는 함수
            break


