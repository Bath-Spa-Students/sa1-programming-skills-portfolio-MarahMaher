dictionary={}
# give commands to the code .

first_name = input ("kindly enter your first name:")
second_name = input ("Kindly enter your second name:")
dictionary['name'] = first_name+" " + second_name 
dictionary['hometown']= input ("kindly enter your hometown: ")

# if your age is digit it will print out if not your should write your digit age .

while True :
    age_input=input("kindly enter your age:")
    if age_input.isdigit ():
        dictionary['age'] = age_input
        print (f"Name: {dictionary['name']} \nHometown: {dictionary['hometown']} \nAge: {dictionary['age']}")
        break
    else:
        print("invalid input. kindly enter a numeric value for age.")

        print("invalid input. kindly enter a numeric value for age.")
