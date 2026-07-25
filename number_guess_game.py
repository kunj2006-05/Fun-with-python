import random

a=int(input("Enter The Range Start From:- "))
b=int(input("Enter The Range End at:- "))
count=0

if a>b:
    print("Invalid range retry the game")
else:    
    num = random.randint(a,b)
    
while True:
    count+=1

    guess=int(input("Enter the your guess: "))
    
    if guess==num:
        print("congratulation!you guess it right")
        print(f"your score is {count}")
        break 
    elif guess>num:
        print("You guessed too high!")
    else:
        print("You guessed too low!")    
    