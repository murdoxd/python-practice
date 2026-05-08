import random
secret = random.randint(1, 100)
attempts = 0
while True:
    user_input = int(input("enter the number: "))
    if user_input == secret:
        print("You guessed!")
        break
    elif user_input > secret:
        attempts += 1
        print(f"Too high {3 - attempts} attempts remaining")
        if attempts == 3:
         print(f"Game over, the number was {secret}")
         break

    elif user_input < secret:
        attempts += 1
        print(f" Too low {3 - attempts} attempts remaining")
        if attempts == 3:
         print(f"Game over, the number was {secret}")
         break
   
