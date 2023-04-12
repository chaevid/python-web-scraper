from random import randint
print("Welcome to the Python Casino!\nGuess a number between 1 and 100")

pc_choice = randint(1, 100)
user_choice = int(input(f"Choose number : "))

while user_choice != pc_choice:
    print("Lower!") if (user_choice > pc_choice) else print("Higher!")
    # if (user_choice > pc_choice):
    #     print("Lower!")
    # else:
    #     print("Higher!")
    user_choice = int(input("Choose number :  "))

print("You win!")
