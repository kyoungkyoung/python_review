print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

# if height > 120:
if height >= 120:
  print("you can ride the rollercoaster!")
  age = int(input("What is your age? "))
  if age < 12:
    print("please pay $5")
  elif age <= 18:
    print("please pay $7")
  else:
    print("please pay $12")
else:
  print("Sorry, you have to grow taller before you can ride")

#comparision operator
# > < >= <= == != %(나머지)
number = int(input("typing the number"))
if number % 2 == 0:
  print("This is an even number.")
else:
  print("This is an odd number.")



# Enter your height in meters e.g., 1.55
height = float(input("what is your height"))
# Enter your weight in kilograms e.g., 72
weight = int(input("what is your weight"))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = weight / (height ** 2)

if bmi < 18.5:
  print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
  print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
  print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
  print(f"Your BMI is {bmi}, you are obese.")
else:
  print(f"Your BMI is {bmi}, you are clinically obese.")


# 윤년 계산기
# Which year do you want to check?
year = int(input())
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
first = year % 4
second = year % 100
third = year % 400

if first == 0:
  if second == 0:
    if third == 0:
      print("Leap year")
    else:
      print("Not leap year")
  else:
    print("Leap year")
else:
  print("Not leap year")
  