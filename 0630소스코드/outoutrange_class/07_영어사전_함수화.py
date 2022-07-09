#영어사전함수화

# 메뉴 만들기
# 영어단어 입력
# 영어사전 단어 및 뜻 입력하기
# 영어단어 탐색하기
# 종료
# 영단어 -key 의미- value로 받은 값은 딕셔너리에 저장
# q누르면 종료

# 빈사전
ek_dic = {}

# 1. 영어단어 등록하기
# ======================== 영단어 생성========================
def input_dict():
    eng = input("영어 단어 입력('q'입력시 초기화면) : ")
    if eng == 'q' :
        pass # 'q' 입력시 해당 if 문을 pass하여 다음을 진행한다.
    elif eng not in ek_dic : # 이미 있는 등록한 단어가 있는지 조사
        kor = input("{}의 뜻을 입력해주세요. : ".format(eng))
        ek_dic[eng] = kor
        input_dict()
    elif eng in ek_dic : # 단어가 이미 등록되어 있으면 수정 or 건너뛰기 선택
        print("{}의 뜻은 {}로 등록 되어 있습니다.".format(eng,ek_dic[eng]))
        # 번호 선택
        input_dict_menu = eval(input("======== 메뉴를 선택 해주세요========="
                                "\n1. 새로운 단어 등록\n2. 단어 수정 및 삭제"
                                "\n숫자입력 1/2: "))
        # 1. 새로운 단어 등록
        if input_dict_menu == 1 : #새로운 단어 입력
            input_dict()
        # 2. 단어 수정 및 삭제

         # 2-1 단어 수정 ed_dict
        elif input_dict_menu == 2:
            ed_dict = eval(input("1. 수정 \n2. 삭제\n3. 초기화면"
                                 "\n숫자입력 1/2/3 : "))
            if ed_dict == 1 :
                rekor = input("%s의 뜻을 입력해주세요 : " % eng)
                ek_dic[eng] = rekor
                input_dict()
         # 2-2 단어 삭제
            elif ed_dict == 2 :
                del ek_dic[eng]
            elif ed_dict == 3 :
                input_dict()
            else :
                pass
# ===========================================================================

# 2. 영어단어 검색하기
# ===========================================================================
def search_dict() :
    search_eng = input("원하시는 단어를 입력 하세요(초기메뉴이동 : q ) : ")
    if list(ek_dic.keys()).count(search_eng) >= 1 :
        print("{}의 뜻은 {}입니다.".format(search_eng,ek_dic[search_eng]))
        search_dict()
    else :
        print("등록되지 않은 단어입니다. 초기화면으로 이동합니다.")
    pass
# ===========================================================================

# 초기메뉴화면
while True :
    print("1. 영어단어 등록하기(1)\n2. 영어단어 검색하기(2)\n3. 종료하기(3)")
    menu = eval(input("숫자 입력 1/2/3 : "))
    if menu == 1 : # input_dict()
        input_dict()
    elif menu == 2 : # search_dict
        search_dict()
    elif menu == 3 :
        break
    else :
        print("정해진 숫자만 입력 가능합니다. 프래그램을 종료합니다.")
        break

