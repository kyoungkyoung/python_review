#n개의 줄로 구성된 직각삼각형 모양의 별을 출력합니다. n이 5인 경우 출력은 다음과 같습니다.
# n = int(input("입력을 원하는 줄 수를 적어주세요"))


# 3번 문제 : 회문 검사
# 문자열이 있을 때 대소문자 상관 없이 그 문자열이 회문인지 여부를 판단하세요.

word  = "토마토"
word_len = len(word)
result = True
cnt = 0

for i in range(word_len // 2):
  if(word[i] != word[(word_len-1) - i]):
    cnt=cnt+1

if(cnt != 0):
  result = False

print(result)



# 4번 문제 : 리스트 내 중복 제거
# 리스트 내부에 있는 중복 요소를 제거하세요. 첫 번째 방법은 set을 사용하고, 두 번째 방법은 for문을 사용하여 직접 제거합니다.
li = [3,3,3,4,5,6,7,8]
set_result = set(li)
print(set_result)

li_len = len(li)
new_li = []
new_li.append(li[0])

for i in range(li_len-1):
  if(li[i] != li[i+1]):
    new_li.append(li[i+1])

print(new_li)

# 5번 문제 : 리스트 뒤집기
# 주어진 리스트를 두 가지 방법으로 뒤집으세요. 첫 번째 방법은 리스트의 내장 메소드를 사용하고, 두 번째 방법은 while문을 사용하여 직접 뒤집으세요.
li2 = [3,3,3,4,5,6,7,8]
li2.reverse()
print(li2)

li3 = [3,3,3,4,5,6,7,8]
li3_len = len(li3)
print(li3_len)
new_li3 = []
cnt3 = 0
while cnt3 < li3_len:
  new_li3.append(li3[(li3_len-1)-cnt3])
  cnt3 = cnt3+1
print(new_li3)


# 6번 문제 : 투표 취합
# n명의 사람이 apple, banana, cherry, grape, orange 5가지 과일 중 하나를 선택한 리스트가 있습니다. 어떤 과일이 몇 표를 받았는지 취합하는 딕셔너리를 만들세요.
# 예) ['cherry', 'grape', 'orange', 'banana', 'cherry', 'banana', 'cherry', 'cherry','apple','apple'] -> {'cherry':4, 'grape':1, 'orange':1, 'banana':2,'apple':2}
