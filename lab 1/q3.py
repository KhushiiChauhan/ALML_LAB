# Prompt the user to enter their name
name = input("Enter your name here: ")

# Greet the user
greet = f"Hello, {name}! Nice to meet you!!"
print(greet)

# Calculate and print the user's age based on their birth year
dob = int(input("Enter your year of birth: "))
current_year = 2024
age = current_year - dob
print(f"Currently, your age is: {age}")
