# here we will make a dictionary .
month_days = {
1 : 31 , #January
2 : 28 , #February
3 : 31 , #March
4 : 30 , #April
5 : 31 , #May
6 : 30 , #June
7 : 31 , #July
8 : 31 , #August 
9 : 30 , #September
10 : 31 , #October 
11 : 30 , #November 
12 : 31 , #December
} 

# user input .
month = int( input("enter the month number:"))
# now we will check the output 
if 1 <= month <= 12:
    print(f"avalible month and it has {month_days[month]} days.")
else :
    print("month number is not correct ")