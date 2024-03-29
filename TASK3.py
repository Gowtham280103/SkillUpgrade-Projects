import random

secret_number = random.randint(1, 100)

guesses = 0

print("Welcome to the Guessing Game!")
print("Guess a number between 1 and 100.")

while True:
    guess = int(input("Enter your guess: "))
    
    guesses += 1
    
    if guess == secret_number:
        print(f"Congratulations! You've guessed the right number ({secret_number}) in {guesses} guesses.")
        break
    elif guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
