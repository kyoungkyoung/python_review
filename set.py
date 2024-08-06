#set는 동일한 값을 중복해서 저장하지 않음 -> 유일한 값을 가짐
#원소의 순서가 없어 인덱스로 접근 불가

set1 = {1,2,3,4,5}
set2 = {3,4,5,6,7}

#합집합
print(set1 | set2)
print(set1.union(set2))

#교집합
print(set1 & set2)
print(set1.intersection(set2))

#차집합
print(set1 - set2)
print(set1.difference(set2))

li = [3,3,3,4,5,6,7]
tu = (3,3,3,4,5,6,7)
dic = {'a':1, 'b': 'hi', 'c': 3}

print(set(li))
print(set(tu))
print(set(dic))