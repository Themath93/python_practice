# #  동일한 이름을 갖는 원소들의 연속 저장 영역
# #  여러 개의 데이터가 저장되어 있는 장소 (집합적 자료
# # 형)
# #  각 원소는 인덱스(Index)로 구분(인덱스: 0부터 시작)
# #  원소(값) 변경 가능 – 부분(원소)변경 가능
# #  리스트 생성 시 대괄호 [ ] 사용
# #  리스트 = [값1, 값2, . . . ]
# #  scores = [ 32, 56, 64, 72, 12]
#
scores = [ 32, 56, 64, 72, 12]
#
# print(id(scores))
# print(type(scores)) # 타입은 list
# print(type(scores[0])) # type is int
#
# print(scores)
# print(scores[0])
# print(scores[1:]) # index 1번부터 출력
# print(scores[1:3]) # scores[n1:n2] > index n1번부터 n2-2 개까지 리스트로 출력 한개만 출력 시 int타입으로 출력
# print(scores[1:4])
#
# print(len(scores))
# for i in range(0,len(scores)) : #0부터 len(scores)-1 의 index번호에 해당하는 값 출력
#     print(scores[i],end=" ")
# print()
# for score in scores :
#     print(score)
sumI = 0

for i in range(0,len(scores)) :
    sumI = sumI + scores[i]
aver_sum = sumI / len(scores)
print("총점은 %d점이며, 평균은 %.1f점 입니다." %(sumI,aver_sum))
