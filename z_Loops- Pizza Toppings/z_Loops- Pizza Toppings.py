# Loop to prompt the user for pizza toppings
while True:
    enter = input("Please enter your flavor (or type 'exit'): ").strip().lower()
    
    if enter == 'exit':
        print("Thank you! We'll start preparing your pizza.")
        break
    else:
        print(f"I'll add {enter} to your pizza.")