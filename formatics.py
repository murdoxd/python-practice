age = int(input("Enter your age: "))

while age < 0 or age > 120:
    print(f"age of {age} is not valid")
    age = int(input("Enter your age: "))


print(f"You are {age} old")