from random import random
user_choice = int(input("Choose number . "))
pc_choice = random.randint(1,50)

if user_choice == pc_choice:
    print("You won!")
elif user_choice > pc_choice:
    print("Lower!")
elif user_choice < pc_choice:
    print("Higher!")