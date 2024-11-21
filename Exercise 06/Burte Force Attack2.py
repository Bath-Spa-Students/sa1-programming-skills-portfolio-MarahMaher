# write the password and how many attempts the user can use .
your_password = "12345"
max_trys = 5
trys_left = 5

# write a while loop to keep the user entering the password .
while trys_left > 0:
    password = input(f"Enter your password. You have {trys_left} trys remaining: ")
    
    if password == your_password:
        # if the user entered the right password this will show .
        print("Password is accepted. Welcome!")
        break  # Exit if the correct password is entered .
    
    trys_left -= 1

    if trys_left == 0:
        #If no trys are left, inform the user that .
        print("The authorities have been alerted. please try again later.")
