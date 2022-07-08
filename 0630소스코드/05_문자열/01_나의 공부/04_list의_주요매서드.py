# 리스트 주요 메소드(함수)
#  len() / count() : 원소(요소)의 개수관련
#  Append() / insert() : 리스트에 원소 추가 관련
#  Remove() / pop() : 리스트 원소 제거 관련
#  Extend() : 리스트의 확장(append/insert와 관련)
#  Sort() / reverse() : 리스트 정렬 및 순서변경과 관련
#  Index() : 특정 요소의 위치값 관련
#  min() / max() : 리스 요소중 최소/최대값 관련
#
# a = [1,2,3,4,5,3,31]
# # print(len(a))
# # print(a.count(3))
#
# a.append(1) # 요소하나만 추가 가능 2개 이상은 에러
# print(a)
# a.insert(0,123)
# print(a)
# a.insert(0,[1,2,3,4,5])
# print(a)
# i = 0
# while i <= len(a)-1:
#     print(a[i])
#     i += 1
# print()
# for b in a:
#     print(b)

# word = "My hobby is python programming"
#
# print(len(word))
# print(word.find("prog"))
# print(word.count('i'))
# print(word.index(("i")))

# 로또번호생성?
# import random
# lotterys = []
# for i in range(5):
#     lotterys.append(random.sample(range(1,45),6))
#     print(lotterys[i])

# ae = []
# for i in range(3):
#     ae.append(input("회원 입력 : "))
# print("회원 명단 : ",end="")
# for a in ae :
#     print(a,end=" ")

# 3 다없애기
n = [1,2,3,3,3,4,5,6,7]

print(n)
print(n.count(3))

for i in range(n.count(3)):
    n.remove(3)
    print("3 삭제", n)
print(n)

