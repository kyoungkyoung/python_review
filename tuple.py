#tuple은 불변성 -> 한번 생성되면 값을 변경할 수 없음

my_tuple = (1,2,3,4,5)
print(my_tuple)
# print(my_tuple[0])


a,b,c = (1,2,3)
print(a,b,c)

a = 5
b = 10

a,b = b,a
print(a,b)