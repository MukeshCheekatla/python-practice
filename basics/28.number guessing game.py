
# Python number guessing game

import random

lowest_num = 1
highest_num =100
answer = random.randint(lowest_num,highest_num)
guesses = 0
is_running= True

print("Python number guessing game")
print(f"Select a number between {lowest_num} and {highest_num}")

while is_running:

    guess = input("Enter your guess: ")

    if guess.isdigit():
        guess= int(guess)
        guesses+=1

        if guess < lowest_num or guess > highest_num:
            print("Out of range")
            print(f"Select a number between {lowest_num} and {highest_num}")
        elif guess < answer:
            print("tooo low")
        elif guess > answer:
            print("too high")
        else:
            print("Correct")
            print(f"no of gueeses {guesses}")
            is_running= False

    else:
        print("Invalid Guess")
        print(f"Select a number between {lowest_num} and {highest_num}")



