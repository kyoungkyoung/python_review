programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

#Retrieving items from dictionary.
print(programming_dictionary)
print(programming_dictionary["Function"])

#Adding and Editing new items to dictionary
# programming_dictionary["Loop"] = "The action of doing something over and over agian."

#Create an empty dictiionary
# empty_dictionary = {}

#Wipe an existing dictionay -> 초기화.. -> 게임 로그지울때!
# programming_dictionary = {}


#Edit an item in a dictionay
# programming_dictionary["Bug"] = "A moth in your computer"

programming_dictionary[1] = "A moth in your computer"
print(programming_dictionary)
# print(programming_dictionary)
#Loop through a dictionary
# for key in programming_dictionary:
#     print(key) #dictionary를 for문 돌리면 key값만 출력된다
#     print(programming_dictionary[key])


    
# dict = {
#     "a": 1,
#     "b": 2,
#     "c": 3,
# }

# dict[1] = 4
# print(dict) #{'a': 1, 'b': 2, 'c': 3, 1: 4}



#method
# dict.clear() - 모든요소 제거
# dict.copy() - 딕셔너리 복사본 반환
# dict.items() - 모든 키-값 쌍 반환
# dict.keys() - return all keys 
# dict.values() - return all values
# dict.get() - 키에대한 값 반환 -> err 내지 않고, None 을 return
# dict.pop() - 키-값 쌍 제거
# dict.fromkeys() - iterable의 각 요소를 키로 사용하여 딕셔너리 생성

# key값은 고유하고, 유일해야한다.
# key 값이 중복되면 마지막에 저장된 value 값이 저장된다.
# dic = { 1: 'a', 1: 'b'}
# print(dic) # dic={1:'b'}

# in -> 해당 key가 딕셔너리 안에 있는지 확인in
# True / False 로 return
# a = {'name':'pey', 'phone':'010-9999-1234', 'birth': '1118'}
# print('name' in a) #true
