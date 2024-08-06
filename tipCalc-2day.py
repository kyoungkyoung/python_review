#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇


#input은 print로 써줄 필요 없음 -> 알아서 print의 기능까지 함
print("Welcome to the tip calculator.")

total_bill = float(input("What was the total bill? $"))
tip_percent = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

total_pay = total_bill * (1+tip_percent/100)
pay = round(total_pay / people, 2)
pay_per_person = total_pay / people

pay2 = "{:.2f}".format(pay_per_person)

print(type(pay2)) #<class 'str'> format 함수는 string으로 바꿔줌

print(f"Each person should pay: ${pay}") #33.6
print(f"Each person should pay: ${pay2}") #33.60
print(f"Each person should pay: ${round(pay_per_person, 2)}") #33.6


