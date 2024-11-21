def even_odd_check(number):
    
    if number % 2 == 0:
        return f"The number {number} is even."
    else:
        return f"The number {number} is odd."

def main():
   
    try:
        # Ask the student for a number to check 
        student_input = int(input("Enter the number: "))
        # the define we did before we will use it here .
        result = even_odd_check(student_input)
        # after the student puts the number print the result to tell if even or odd .
        print(result)
    except :
        print("Input not correct .")

# Run the main function .
if __name__ == "__main__":
    main()
