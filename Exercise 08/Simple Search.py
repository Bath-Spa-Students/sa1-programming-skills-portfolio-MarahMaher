# enter users name 
user_name = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

search_name = "Ian"
if search_name in user_name : 
    print(f'"{search_name}" is found in the list ')
else:
    print(f'"{search_name}" is not found in the list.')

# The user can search for the name if its in the list it will show found .
# if the name is not in the list it will show not found.

input_user = input("Enter a name to search for: ").strip()
if input_user in user_name:
    print(f'"{input_user}" is found in the list!')
else:
    print(f'"{input_user}" is not found in the list.')