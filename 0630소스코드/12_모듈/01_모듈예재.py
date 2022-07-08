#생성해 놓은 모듈 new_calculator import
import new_calculator # 현재 파일과 동일한 디렉토리내에 존재하므로 자동 완성가능

#모듈내 특정 함수 import
from new_calculator import *

a = new_calculator.add(7,4)
print(a)

s = sub(7,4) # 함수자체를 불러오면 함수만 입력해도 사용가능
print(s)

m = mul(7,4)
print(m)
m1 = new_calculator.mul(7,4)
print(m1)