
# Find the first and last element of the list [3,0,1,10,-2,8,12]
list1 = [3,0,1,10,-2,8,12]
print("First Element of List is", list1[0])
print("Last Element of List is", list1[-1])


# Find the length of the string “hyderabad”
print("Length of String 'hyderabad' is ", len("hyderabad"))

# Add the strings “python” and “programming”
x = "python"
y = "programming"
print(x + " " + y)

# Find the third character in the string “Final year”
x = "Final year"
print("Here 3rd Character is",x[2])

# Print the last two characters of the string “MSIT”
x = "MSIT"
print(x[2:])

# Print "INDIA" in reverse order from the string “MSITHYDINDIA”
x = "MSITHYDINDIA"
print(x[-1:-6:-1])


# Print the first 7 characters of the string “I am a programmer”
x = "I am a programmer"
print(x[0:7])

# Usage of strip() method
b = "      Face Book       "
a=b.strip()
print("After Strip :",a)

# Print Max Number from numbers
x,y,z = 2,3,4
print(max(x,y,z))

# Assign 100 to a,b,c in one go
a = b = c = 100
print(a,b,c)

# Find Biggest Number
a=int(input("Enter your first Number : "))
b=int(input("Enter your 2nd Number : "))
c=int(input("Enter your 3rd Number : "))
if a==b==c==0:
    print ("you have entered 0 for a,b,c")
elif a>b & a>c:
    print (a,"is the Biggest Number ")
elif b>c:
    print (b,"is the Biggest Number")
else:
    print (c,"is the Biggest Number")


# Usage of round() method
# this will round off to next integer (+ve)
print(round(3.5))
print(round(11/2))


#Create Global variable outside of fuction , then modify that variable within function. condition : modified variable must be use globally again
x = "I'M BRAND NEW GLOBAL VARIABLE"
print("HELLO Global Variable Declared in Outside of Function, : " + x)
def myfunc():
  global x
  x = "I'M MODIFIED GLOBAL VARIABLE"


myfunc()
print("Global Variable Replaced with in Function, then use globally Here : " + x)