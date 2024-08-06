'''
#List

states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", 
                     "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", 
                     "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", 
                     "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", 
                     "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", 
                     "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", 
                     "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", 
                     "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", 
                     "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

# print(states_of_america[0])
# print(states_of_america[-1]) #Hawaii -> 가장 마지막 항목이 출력 
# print(states_of_america[1:3]) #['Pennsylvania', 'New Jersey'] -> 1번부터 2번까지 출력

#add -> 가장 마지막에 추가(1개만 추가 가능)
# states_of_america.append("wkland") 
# states_of_america.extend(["wkland", "Angelaland"])
# states_of_america.insert(1,"wk")
#print(states_of_america)

#delete
# del states_of_america[0]

num_of_state = len(states_of_america)
print(states_of_america[num_of_state - 1])



name_string = "Angela, Ben, Jenny, Michael, Cloe"
names = name_string.split(", ")

# print(names)

import random

cnt = len(names)
#print(cnt)

random_num = random.randint(0, cnt-1)
random_person = names[random_num]

# print(f"{random_person} is going to buy the meal today!")

# list.append(100) - 맨뒤에 값(100) 추가
# append()는 리스트에 요소 1개씩을 추가해야 함 -> 여러개 추가 못함
a = [1,2,3,4,5]
a.append(6)
# [7,8] 이 리스트 자체가 하나의 값으로 append
a.append([7,8])

# list.insert(3,100) - 원하는 위치(3)에 값(100) 추가

# list.remove(5) - 해당하는 값(인덱스가 아닌 값이 5) 삭제
# 값이 중복되는 경우 앞의 index값이 삭제
d = [1,2,3,3,4]
d.remove(3)
print(d)

# list.pop(2) - 해당 위치 값(2) 삭제 -> 값 안넣으면 마지막 값 삭제
# list.sort() - 리스트 내부 값 정렬 -> 기본 오름차순 / list.sort(reverse=True) -> 내림차순 정렬 -> return 값은 None
# sorted(list)
# list.reverse() - 순서를 그대로 앞뒤로 뒤집기, 내림차순 정렬 X

# list.index(9) - 해당 값(9)의 위치 반환 / 값이 없다면 err return
# 값이 중복되는 경우에는 앞의 index값이 출력
b = [1,2,3,3]
print(b.index(3))

# list.count(1) - 해당 값(1)의 개수 반환

# list.extend(list)- 리스트 합치기
# 중복되는 값은 삭제되지 않고 값이 2개가 된다
g = [1,2,3,4]
h = [4,5,6]
g.extend(h)
print(g)


# Iterable : 순회 가능한 객체를 나타내는 용어
# len(iterable)
# sum(iterable)
# max(iterable)
# min(iterable)

# boolean list 에서 사용
# any(iterable) #list 안쪽에 하나라도 true가 있으면 true return
# all(iterable) #list 안쪽의 모든 요소가 true일 경우만 true return



text_list = list('hello')
print(text_list) #['h', 'e', 'l', 'l', 'o']



# join()
li = ['a','b','c']
text = ''

for i in li:
    text += i

print(li)
print(*li)
# print(type(*li)) # error
print(''.join(li)) # abc
print('-'.join(li)) # a-b-c


'''
a = [1, 10, 5, 7, 6]
a.sort() # return None

print(sorted(a))

# a = [1, 10, 5, 7, 6]
# a.sort(reverse=True)

