import random
import words
# word_lists = ['ardvark','baboon','camel']
chosen_word = random.choice(words.words)
print(f'Pssst , the solution is {chosen_word}')
display = ['-' for i in range(len(chosen_word))]

end_of_game = False
lives = 6
value = True
while not end_of_game:
    print(" ".join(display))
    print(f"You have {lives} live ")
    guess = input("Guess a letter: ").lower()
    if guess not in display:
        for position in range(len(chosen_word)):
            letter  = chosen_word[position]
            # print(f"""Current position: {position}
            # \n Current letter: {letter}\n Gusessed letter:{guess}""")
            if letter == guess:
                display[position] = guess
    else:
        print("This guess letter already used!")
            
    if guess not in chosen_word:
        lives-=1
        if lives == 0:
            end_of_game= True
            print("You lose.")

    if '-' not in display:
        end_of_game = True
        print(" You Win Game! ")
    # if lives == 0:
    #     end_of_game = True
    #     print(" You Lose Game! ")

    # print(stages[lives])