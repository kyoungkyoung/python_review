line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇
letter = position[0].lower()
abc = ["a", "b", "c"]
column_num = abc.index(letter) #index()는 괄호 안의 값이 있으면 해당 인덱스 값을 알려줌 
# aa = abc.index("d")

# pirnt(aa)

row = int(position[1]) - 1


map[row][column_num] = "X"
# print(map)
# print(map[0][0])

# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")