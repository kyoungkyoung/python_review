#Data Types

#String

print("Hello"[1])
text = '123456789'

print(text[::-1]) #987654321 -> 글자 뒤집기
print(text[-2:-6:-1]) #8765
print(text[-2:-6:]) #아무런 값도 출력하지 않음 -> err 도 안냄

textStr = 'qwer'
print(min(textStr))
print(max(textStr))

# string 정렬
name = '홍길영'
age = 32

print(f'제 이름은{name:<5}이고 나이는 {age}입니다.') # 5자리 차지, 오른쪽 정렬
print(f'제 이름은{name:>5}이고 나이는 {age}입니다.') # 5자리 차지, 왼쪽 정렬
print(f'제 이름은{name:^5}이고 나이는 {age}입니다.') # 5자리 차지, 가운데 정렬
print(f'제 이름은{name:<5}이고 나이는 {age:8.2f}입니다.') # 8자리 차지, 소수점 아래 2개표기
print(f'제 이름은{name:<5}이고 나이는 {age:.2f}입니다.') # 소수점 아래 2개표기



#Integer
# print(123+456)
# print(123_456_789) #_는 안보이게 된다! -> 1000단위 ,표시 대신 사용하면 편함!!

#Float
3.141592

#Boolean
True
False

#type check
num = 123
# print(type(num)) # <class 'int'> -> Integer

#type casting
num_char = str(num)
num_float = float(num)

# print(num_char)
# print(type(num_char)) # <class 'str'> -> String
# print(type(num_float))

text = 'Today is July'
# print(text[0:5]) #Today -> 0부터 4까지 출력



#연산
3 + 5
7 - 4
3 * 2
6 / 3 #나눗셈을 하면 항상 실수 형태로 출력 -> 모든 형태의 연산에 나누기가 한번이라도 들어가면 실수 출력
2 ** 2 # 거듭제곱 표시 -> 4
2 ** 3 # 8

# print(2**2)
# print(2**3)

# number Format , round(), floor division //
8 / 3 #2.666666
round(8/3) #2.7
# print(round(8 / 3, 2)) #2.67 -> 8/3 의 값을 소수 점 아래 2째자리 수까지 반올림 해서 표기
# print(8 // 3) #2 -> // 두개는 소수점 아래 버림 = floor -> type은 int

# += , -= , /= *=
result = 4 / 2
result /= 2 #result = result / 2

cnt = 0
cnt += 1 #score = score + 1

score = 0
height = 1.8
isWinning = True

#print("your score is " + str(score))

#f-String -> convert all type variables to String!!
# print(f"your score is {score}, your height is {height}, you are winning is {isWinning}")

# print(1*2)
# print(6+4/2-(1*2))
