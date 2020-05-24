#Design Small Calculator for any 2 numbers , calculator can perform addition, subtraction, multiplication, division , must be take input from user

a=int(input("Hello This is Small Calculator, It's Working for any 2 numbrers only, \n Here 4 Operations Available \n 1.Addition \n 2.Subtraction \n 3.Division \n 4.Multiplication \n According your need please enter Operation Number corrosponding number to go further \n Please Enter Your Selection Here : "))

if a==1:
    x = int(input("Enter 1st number : "))
    y = int(input("Enter 2nd number : "))
    add2num = x + y
    print("Addition of These two numbers is : ", add2num)
elif a==2:
    x = int(input("Enter 1st number : "))
    y = int(input("Enter 2nd number : "))
    add2num = x - y
    print("Subtraction of These two numbers is : ", add2num)
elif a==3:
    x = int(input("Enter Dividend : "))
    y = int(input("Enter Divisor : "))
    add2num = x / y
    print("Division of These two numbers is : ", add2num)
elif a == 4:
    x = int(input("Enter 1st number : "))
    y = int(input("Enter 2nd number : "))
    add2num = x * y
    print("Multiplication of These two numbers is : ", add2num)
else:
    print("Please Enter valid input as 1 or 2 or 3 or 4 only")