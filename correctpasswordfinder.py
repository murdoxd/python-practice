correct_password = "ClaudeCode"
attempts = 0

while True:
   user_input = input("Enter the password: ")
   if user_input == correct_password:
      print("Correct")
      break
   else:
    attempts += 1  
    print(f"Wrong password. {3 - attempts} attempts remaining.")
    if attempts == 3:
       print("You have tried too many times")
       print("Account locked")
       break
    