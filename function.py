# 함수 명명
'''
def my_function():
    print("Hello")
    print("Bye")

def greet(name):
    print(f"Hello {name}")

greet("wk")

# name - parameter / wk - argument

'''
'''
#Functions with more than 1 input
def greet_with(name, location, age):
    print(f"Hello {name}")
    print(f"What is it like in {location}")
    print(f"You are {age} years old")

# greet_with("wonkyoung", "Seoul", 31)
greet_with(location="Seoul", age=31, name="wonkyoung")


# Write your code below this line 👇
def prime_checker(number):
  cnt = 0
  for i in range(2, number):
    if number % i == 0:
      cnt += 1
  if cnt == 0:
    print("It's a prime number.")
  else:
    print("It's not a prime number.")
 


# Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input()) # Check this number
prime_checker(number=n)



# Write your code below this line 👇
def prime_checker(number):
  is_prime = True
  for i in range(2, number):
    if number % i == 0:
      is_prime = False
  if is_prime:
    print("It's a prime number.")
  else:
    print("It's not a prime number.")
 


# Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input()) # Check this number
prime_checker(number=n)

'''







def my_function2():
  print("Hello")
  print("bye")

my_function2()