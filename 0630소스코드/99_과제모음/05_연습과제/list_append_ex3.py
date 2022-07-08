#  80점 이상 학생의 수를 계산하여 출력

scores = []
sum_scores = 0

for i in range(1,6) :
    score = eval(input("학생{} 점수 입력 : ".format(i))) # 학생별로 점수 입력받기
    scores.append(score) # 입력받는 학생 순서대로 scores 리스트에 요소로 넣어주기
    sum_scores += score
cutline = eval(input("커트라인 점수 입력 : "))
over_cutline = 0
for d in range(len(scores)) :
    if scores[d] >= cutline :
        over_cutline += 1
    else :
        continue
average_scores = sum_scores/5
print("총점 : %d" % sum_scores)
print("평균 : %.2f" % average_scores)
print("%d점 이상 학생 : %d명" % (cutline,over_cutline))

