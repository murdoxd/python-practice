secret = 20
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
         print("Game over, the number was 20")
         break

    elif user_input < secret:
        attempts += 1
        print(f" Too low {3 - attempts} attempts remaining")
        if attempts == 3:
         print("Game over, the number was 20")
         break
   