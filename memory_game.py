import random
import time
import os

seconds = 5
points = 0

while seconds > 0:
    print(f"""Welcome to 'Memory Game'!

There are 10 levels.
        
Correct guess will give you 2 point.
Incorrect guess will give you -1 point.
    
You don't have to put spaces between numbers.
        
>> Starting in {seconds} seconds.
        
        """)
    time.sleep(1)
    seconds -= 1
    os.system("cls")

random_numbers = []
for i in range(1,11):
    new_random_number = random.randint(1, 9)
    random_numbers.append(new_random_number)
    print(f"(Level {i}):",*random_numbers)
    time.sleep(i/2)    # Time slowly increase when the numbers are increase.
    os.system('cls')

    guess = input("What were the numbers? ")
    if guess == "".join(str(x) for x in random_numbers):
        print("Correct! +2 Points.\n")
        points += 2
    else:
        print(f"Incorrect. -1 Points. The numbers were: {''.join(str(x) for x in random_numbers)}.\n")
        points -= 1

print(f"Game Over! You got {points} points.")
