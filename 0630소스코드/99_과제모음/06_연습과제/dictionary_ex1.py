#  다음과 같이 리스트를 선언하고 각 학생의 총점과 평균 출력

students = [
    {"name": "홍길동", "korean": 87, "math": 98, "english" :88, "science": 95},
    {"name": "이몽룡", "korean": 92, "math": 98, "english": 96, "science": 98},
    {"name": "성춘향", "korean": 76, "math": 96, "english": 94, "science": 90},
    {"name": "변학도", "korean": 98, "math": 92, "english": 96, "science": 92},
    {"name": "박지성", "korean": 95, "math": 98, "english": 98, "science": 98},
    {"name": "류현진", "korean": 64, "math": 88, "english": 92, "science": 92}
]
# list(students[i].values()`)[j] # j를 0으로 고정하면 i가 돌면서 이름만 출력
# list(students[i].values()`)[j] # i가 고정된 상태에 j만 돌면서 점수들 출력
sum_scores = 0
a = 0
print("%s \t %s \t %s" % ("이름", "총점", "평균"))
for i in range(6) :
    for j in range(1,5) :
        a += list(students[i].values())[j] # 점수더하기
    c = a/4 # 평균구하기
    print("{} \t {} \t {}".format(list(students[i].values())[0],a,round(c,2)))
    a = 0 # 다음 학생의 총점구하기 위해 0으로 초기화

