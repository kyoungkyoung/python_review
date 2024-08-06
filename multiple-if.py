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




