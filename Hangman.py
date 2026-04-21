import random
import os
from time import sleep

from wordlist import wordsfood, animals

hangman_art = {0: ("   ",
                   "   ",
                   "   "),
               1: (" o ",
                   "   ",
                   "   "),
               2: (" o ",
                   " | ",
                   "   "),
               3: (" o ",
                   "/| ",
                   "   "),
               4: (" o ",
                   "/|\\",
                   "   "),
               5: (" o ",
                   "/|\\",
                   "/  "),
               6: (" o ",
                   "/|\\",
                   "/ \\")}

def display_man(wrong_guesses):
    print("***************")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("***************")
def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))

def main():
    while True:
        version_input = input("What version do you want? (current: food, animals): ")
        if version_input != "food" and version_input != "animals":
            print("Not a great start! please enter a good version")
        if version_input == "food":
            answer = random.choice(wordsfood)
            hint = ["_"] * len(answer)

            wrong_guesses = 0
            guessed_letters = set()
            is_running = True

            while is_running:
                display_man(wrong_guesses)
                display_hint(hint)
                guess = input("Enter a letter: ").lower()

                if len(guess) != 1 or not guess.isalpha():
                    print("invalid input")
                    continue

                if guess in guessed_letters:
                    print(f"{guess} is already guessed!")
                    continue

                guessed_letters.add(guess)
            
                if guess in answer:
                    for i in range(len(answer)):
                        if answer[i] == guess:
                            hint[i] = guess

                else:
                    wrong_guesses += 1

                if "_" not in hint:
                    display_man(wrong_guesses)
                    display_answer(answer)
                    print("YOU WIN")
                    sleep(3)
                    os.system('cls')
                    break
                elif wrong_guesses >= len(hangman_art) - 1:
                    display_man(wrong_guesses)
                    display_answer(answer)
                    print("YOU LOSE")
                    sleep(8)
                    os.system('cls')
                    break
        if version_input == "animals":
            answer = random.choice(animals)
            hint = ["_"] * len(answer)

            wrong_guesses = 0
            guessed_letters = set()
            is_running = True

            while is_running:
                display_man(wrong_guesses)
                display_hint(hint)
                guess = input("Enter a letter: ").lower()

                if len(guess) != 1 or not guess.isalpha():
                    print("invalid input")
                    continue

                if guess in guessed_letters:
                    print(f"{guess} is already guessed!")
                    continue

                guessed_letters.add(guess)
            
                if guess in answer:
                    for i in range(len(answer)):
                        if answer[i] == guess:
                            hint[i] = guess

                else:
                    wrong_guesses += 1

                if "_" not in hint:
                    display_man(wrong_guesses)
                    display_answer(answer)
                    print("YOU WIN")
                    sleep(3)
                    os.system('cls')
                    break
                elif wrong_guesses >= len(hangman_art) - 1:
                    display_man(wrong_guesses)
                    display_answer(answer)
                    print("YOU LOSE")
                    sleep(8)
                    os.system('cls')
                    break
            

if __name__ == "__main__":
    main()
 