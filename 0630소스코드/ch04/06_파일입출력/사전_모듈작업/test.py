#
# ek_dict = {'dog':'강아지','cat':'고양이','note':'공책'}
#
# "dog,cat,note,-강아지,고양이,공책,"
#
# # 키와 value를 따로 저장
#
# d_key = ek_dict.keys() # 키만 저장
# d_value = ek_dict.values() # value만 저장
#
# print(d_key)
# print(d_value)
#
# result = ''
#
# for k in d_key :
#     print(k)
#     result += k + ','
# result += '-'
# print(result)
# for v in d_value :
#     print(v)
#     result += v +','
# print(result)
# list_result = result.split('-')

# 사전파일에서 data 읽어오는 로직 설명
results = ['dog,cat,-강아지,고양이,'] # 1개의 요소만 있음

if results == [] : #파일에 데이터가 하나도 없어서 하나도 읽어오지 않았을때
    pass
res = results[0].split('-')
print(res) # ['dog,cat,', '강아지,고양이,']

d_keys = res[0].split(',')[:-1] # 맨 마지막 요소를 제외한 나머지 추출

print(d_keys) # ['dog', 'cat']

d_values = res[1].split(',')[:-1]
print(d_values) # ['강아지', '고양이']

# zip 함수 이용해서 딕셔너리 생성
dict_temp = dict(zip(d_keys,d_values))
print(dict_temp) # {'dog': '강아지', 'cat': '고양이'}



# dict_temp를 ek_dict 공용 변수에 저장해야 함
# 일반 대입연산자를 사용해서 전체 값을 바꾸면 지역변수가 생성됨
# 부분변경(부분대입을 이용)
ek_dic = {}
for item in dict_temp.items() :
    print(item)
    k,v = item
    ek_dic[k] =v
print(ek_dic)