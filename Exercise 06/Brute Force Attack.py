
Your_password = "12345"  # Correct password

# Ask the user to enter the password
password = input("Enter your password: ")

# Use a while loop if the user didn't put the correct password 
while password != Your_password:
    password = input("password not correct. Please try again: ")

# Once the correct password is entered
print("Password is correct. Welcome!")

