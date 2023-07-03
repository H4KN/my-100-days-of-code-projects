import random

word_list = ["dagedage", "highhigh","casecase"]

chosen_word = random.choice(word_list)

print(chosen_word)

display = []

for d in range(0, len(chosen_word)):
    display.append("-")
print(display)


chosen_word_list = list(chosen_word)

lives = 0

stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

check = []

while "-" in display:
    guess = (input('enter your letter: ')).lower()
    
    if guess in check:
        print("You've used this letter before, try another!")
    for n in range(0 , len(chosen_word)):
        letter = chosen_word[n]
        if letter == guess:
            display[n] = letter
            check.append(guess)
    print(display)

    if "-" not in display:
        print("YOU WON")
    
    elif guess not in chosen_word:
        if lives == 6:
            print("YOU LOSE")
            print(stages[lives])
        else:
            print(stages[lives])
            lives +=1
    
        







# if chosen_word_list[n] == guess:
#             chosen_word_list[n] = guess
            
#         else:
#             chosen_word_list[n] = "-"

#     chosen_word_list_for = chosen_word_list
#     print(chosen_word_list_for)   
            
#     a += 1
    
#     guess = (input('enter your letter: ')).lower()



# display2 = []

# for letter in chosen_word_list:
#     if letter == guess:
#         print("Yes")
#         display2.append(letter)
#     else:
#         print("No")
#         display2.append('-')
        
        
# print(display2)