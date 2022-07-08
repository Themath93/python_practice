#영어사전함수화

# 영어단어 입력
# 영어사전 단어 및 뜻 입력하기
# 영어단어 탐색하기
# 종료
# 영단어 -key 의미- value로 받은 값은 딕셔너리에 저장
# q누르면 종료
ek_dic = {}


while True :
    eng = input("영어단어 뜻 입력('q'입력시 종료) : ")
    if eng == 'q' :
        break
    elif eng not in ek_dic :
        kor = input("{}의 뜻을 입력해주세요. : ".format(eng))
        ek_dic[eng] = kor
        print(ek_dic)
    else:
        print("{}의 뜻은 {}입니다.".format(eng,ek_dic[eng]))
