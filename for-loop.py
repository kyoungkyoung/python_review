fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
  print(fruit)
  print(fruit + " Pie")
print(fruits)
'''
  Apple
  Apple Pie
  Peach
  Peach Pie
  Pear
  Pear Pie
'''

'''
# input =  156 178 165 171 187
student_heights = input("heigts").split(" ")
sum = 0
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
  sum += student_heights[n]

average = round(sum/len(student_heights))

print(f"total height = {sum}")
print(f"number of students = {len(student_heights)}")
print(f"average height = {average}")
'''

'''
#78 65 89 86 55 91 64 89
# Input a list of student scores
student_scores = input("scores").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
# Write your code below this row 👇

print(max(student_scores))
'''

#For Loop with Range
for number in range(1, 11, 3): #마지막 3은 증가율 -> 1 4 7 10
  print(number) #1 2 3 4 5 6 7 8 9 10 (증가율 안썼을 때) -> 마지막 숫자 포함 안함

total = 0
for i in range(1,101):
  total += i
print(total)


# 구름
def solution(shirt_size):
  size_li = ["XS", "S", "M", "L", "XL", "XXL"]
  answer = [0] * len(size_li)
  print(f'answer = {answer}')
  
  for size in shirt_size:
    for i in range(len(size_li)):
      if size == size_li[i]:
        answer[i] += 1
    
    # if size == 'XS':
    #   answer[0] +=1
    # elif size == 'S':
    #   answer[1] +=1
    # elif size == 'M':
    #   answer[2] +=1
    # elif size == 'L':
    #   answer[3] +=1
    # elif size == 'XL':
    #   answer[4] +=1
    # elif size == 'XXL':
    #   answer[5] +=1

  return answer

solution(["XS", "S", "L", "L", "XL", "S"])