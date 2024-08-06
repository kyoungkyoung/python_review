import random

# module 자체를 import 하는 방식
import my_module 
# chosen_word = random.choice(my_module.word_list)

# module 안의 특정 값 or 함수를 import 하는 방식
from my_module import word_list
chosen_word = random.choice(word_list)


# word_list = ['ardvark', 'baboon', 'camel']

chosen_letter = []
letter_list = []
end_of_game = False
lives = 6

print(f"The answer is {chosen_word}")

for letter in chosen_word:
    chosen_letter.append(letter)
    letter_list.append("_")

print(letter_list)

while not end_of_game:
    input_letter = input('guess a letter : ').lower()

    for i in range(len(chosen_letter)):
        
        # print(letter)
        if input_letter == chosen_letter[i]:
            letter_list[i] = input_letter
            # print("match")
            # print(chosen_letter)
        else:
            print("wrong")
            
    if input_letter not in letter_list:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You Lose")

    print(letter_list)

    if "_" not in letter_list:
        print(letter_list)
        print("You win")
        break

    print(lives)
