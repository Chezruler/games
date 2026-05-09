import random
import os
from time import sleep


def randomnumber():
    randomnumber = random.randint(1, 10)
    return randomnumber

def main():
    while True:
        print("Welcome! this is a small project made by Chez, any tips please give to my discord, i really appreciate it")
        startinput = input("Wanna start playing (y/n): ")
        if startinput == ("y").lower:
            os.system('cls' if os.name == 'nt' else 'clear')
            while True:
                number = input("What number are you choosing? (1/10): ")

                if not number.isdigit():
                    print("Please enter a valid number.")
                    continue

                number = int(number)

                if number > 10 and number < 0:
                    print("Thats not possible, try under 10")
                    continue

                randomdigit = randomnumber()
                
                if randomdigit == number:
                    print(f"You won! The number was {randomdigit}!")
                elif randomdigit != number:
                    print(f"You lost! The number was {randomdigit}!")
                
                playagaininput = input("Do you want to play again?: ")
                if playagaininput == ("y").lower:
                    sleep(1)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    continue
                if playagaininput ==("n").lower:
                    break               
            
        if startinput == ("n").lower:
            break
    

        


if __name__  == "__main__":
    main()
