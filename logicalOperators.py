# and, or, not
# 

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

# if height > 120:
if height >= 120:
  age = int(input("What is your age? "))
  if age < 12:
    bill = 5
    print("please pay $5")
  elif age <= 18:
    bill = 7
    print("please pay $7")
  elif age >= 45 and age <= 55:
    bill = 0
  else:
    bill = 12
    print("please pay $12")

  wants_photo = input("Do you want a photo taken? Y or N ")
  if wants_photo == "Y":
    #Add $3 to ther bill
    bill += 3 #bill = bill + 3
  
  print(f"Your final bill is {bill}")
  # else: 는 여기서 쓸 필요가 없다 
else:
  print("Sorry, you have to grow taller before you can ride")






print("The Love Calculator is calculating your score...")
name1 = input("What is your name?") 
name2 = input("What is their name?") 

combined_names = name1 + name2
lower_names = combined_names.lower() #make lower case
t = lower_names.count('t') # count()는 integer return
r = lower_names.count('r')
u = lower_names.count('u')
e = lower_names.count('e')
first_digit = t + r + u + e

l = lower_names.count('l')
o = lower_names.count('o')
v = lower_names.count('v')
e = lower_names.count('e')
second_digit = l + o + v + e

score = int(str(first_digit) + str(second_digit))

if (score < 10) or (score > 90):
  print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >= 40) and (score <= 50):
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")




