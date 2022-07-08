# 딕셔너리를 이용한 사전 구성 및 사전 검색 프로그램

# 빈 딕셔너리를 생성
ek_dic = dict ={}

# 사전에 단어 등록 프로세스
# 사용자로부터 입력받은 단어와 뜻을 사전에 등록
# 기존에 있는 단어의 등록은 기존에 있다고 알려주고 등록하지 않습니다.
# 종료는 quit를 입력하면 종료 - 무한루프
while True :
    # 영어단어 입력받기
    eng = input("\n영어 단어 등록(종료는 quit) : ")

    # 종료검사
    if eng == "quit" :
        break
    elif eng not in ek_dic :# 입력된 단어가 사전에 있는 단어 인지 검사
        # 뜻을 입력받기
        kor = input(eng + "뜻 입력 : " % eng)
        ek_dic[eng] = kor # 사전에 등록 key를 영단어 value를 의미
    else :
        print("%s는 이미 등록된 단어 입니다." % eng)

print("\n사전 단어 검색을 시작합니다.")

# 완성된 사전 에서 단어를 검색하는 프로세스
# 사용자가 입력한 단어의 뜻을 출력
# 없는단어는 사전에 없다는 정보를 출력
# 종료는 quit을 입력하면 종료 - 무한루프
while True :
    #검색 단어 입력 받기
    eng = input("\n검색할 단어 입력 (종료는 quit) : ")
    # 종료 조건 검사
    if eng =="quit" :
        print('검색을 종료합니다.')
        break
    elif eng in ek_dic :
        print("%s 의 뜻은 %s 입니다. " % (eng, ek_dic[eng]))
    else :
        print("%s는 사전에 없는 단어 입니다. " % eng)

print("\n 종료 합니다.")