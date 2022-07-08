# 튜플 tuple()
# 수정 불가 상수 리터럴 같은느낌 바뀌면 안되는 값을 선언할 때 아주좋다.

t1 = (1,2,3)
t2 = 4,5,6
t3 = t1,4,5,6
t4 = [1,2],[3,4]
t5 = tuple([5,6,7,8])
l1 = [1,2,3,4]
t6 = tuple(l1)
print(type(t1))
print(type(t1[0]))
print(t2)
print(t3)
print(t4)
print(t5)
print(t6)

to_list1 = list(t1)
print(to_list1)
to_list4 = list(t4)
print(to_list4)
to_list2 = list(((1,2),(3,4)))
print(to_list2)

for i in range(3) :
    print(t1[i])