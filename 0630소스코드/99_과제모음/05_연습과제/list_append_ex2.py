#  학생 5명의 점수를 입력 받아서 list에 저장한 후 총점과
# 평균을 구하여 출력

scores = []
sum_scores = 0

for i in range(1,6) :
    score = eval(input("학생{} 점수 입력 : ".format(i))) # 학생별로 점수 입력받기
    scores.append(score) # 입력받는 학생 순서대로 scores 리스트에 요소로 넣어주기
    sum_scores += score

average_scores = sum_scores/5
print("총점 : %d" % sum_scores)
print("평균 : %.2f" % average_scores)


