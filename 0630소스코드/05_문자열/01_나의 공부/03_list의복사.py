# # 얕은 복사
#
# scores = [1,2,3,4,5]
# gene = scores
# print(scores)
# print(gene)
#
# scores[0] = 10
# print(scores)
# print(gene) # gene변수의 리스트에 어떤 변화를 주지 않았지만 리스트 값이 바뀌어있음
# 위 방식의 리스트 복사는 리스트 자체를 복사해서 넣어주는 것이 아닌
# 리스트객체의 주소값만 대입연산자로 넣어주는 것이기 때문에
# 원본의 리스트에 변화가 생기면 참조값만 받은 변수의 값도 변화한다.
#
# #  깊은 복사 (deep copy)
# #  = 연산자만으로는 깊은 복사를 진행 할 수 없음
# #  list() 함수 또는 deepcopy() 함수를 사용해서
# #  리스트의 값의 복사본을 새로 생성하여 반환
# #  복사본 리스트 원소의 값을 변경하여도
# #  원본 리스트 원소의 값은 변경되지 않음
# scores = [1,2,3,4,5]
# values = list(scores)
# print(scores)
# print(values)
# scores[0] = 20
# print(scores)
# print(values)

# deepcopy() : 깊은복사
import copy

a = ['a', 'b', 'c']
c = a
b = copy.deepcopy(a)
print("list a의 값 : ", a)
print("list b의 값 : ", b)
print("list c의 값 : ", c)
print('-------a의변화------')
a[0] = 'z'
print("list a의 값 : ", a)
print("list b의 값 : ", b)
print("list c의 값 : ", c)

