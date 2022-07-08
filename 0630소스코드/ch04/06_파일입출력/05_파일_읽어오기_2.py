# 전체라인 읽어오기
# readlines()

print("-------------- 전체라인 읽고 출력 ------------------")

f1 = open('test.txt','r')
lines = f1.readlines() # 전체 행을 읽어서 list로 변환
for line in lines :
    print(line,end="")
print()
# print(lines) # 각 라인들의 리스트의 요소로 자리잡고 있으며
# 각 리스트 마지막의 \n 는 끝에서 Enter키 입력도 있기 때문 (줄바꿈)
# 마지막 요소인 '4. 파일' 에서 \n가 없는 이유는 마지막에 줄바꿈을 하지 않고 저장했기 때문
f1.close()


print("=========== readlinses() 없이 파일 읽어오기 =============")

f3 = open('test.txt', 'r')

# for의 반복요소로 파일개체 사용가능
for line in f3 :
    print(line,end='')

f3.close()
