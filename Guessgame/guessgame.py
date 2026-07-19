import random

print("Welcome to the Guess the Number Game!")
print("Choose a number between 1 to 100!")
print("Yoy have only 7 attempts to guess the number correctly!")
secret_number=random.randint(1,100)
attempts=7
while attempts>0:
    guess=int(input("Enter your guess : "))
    if guess==secret_number:
        used_attempts=8-attempts
        print("Congratulation! You guess it right!")
        print(f"The number was {secret_number}")
        print(f"You guess the number in {used_attempts} attempts")
        break
    elif guess<secret_number:
        print("Too Low! Try a higher number : ")
    else:
        print("Too High! Try a lower number : ")
    attempts=attempts-1
    print(f"Attempts left! {attempts}")
    if attempts==0:
        print("You have used all your attempts!")
        print(f"The number was {secret_number}")