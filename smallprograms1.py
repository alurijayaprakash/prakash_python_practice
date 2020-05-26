
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

# Print “MSIT” in reverse order
x = "MSIT"
print(x[::-1])

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
'''
in round() method
3.1 ...3.4 will be 3
3.5 ...3.9 will be 4
'''
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


# Using replace() module replace char from string
a = "Hello Prakash"
print(a.replace("Hello", "Hi"))
print(a.replace("H", "h"))

# Using replace() module replace int digit from integer
# Hint : we can't replace int , so type cast then replace.
a = 34
b = str(34)
c=b.replace('3','5')
print(int(c))
print(type(int(c)))

# Using split() function split two strings based on a separator
# Observations : finally we will get output list which contain those two substrings
# we can't use "\"
x = "Hello,Prakash"
print(x.split(","))

# In List, Here the process of replacing a List item
a = ['Hello Prakash', (2+3j), 2, 5.6]
print("Actual List is :",a)
a[1] = 6
a[2] = "USA"
print("1st Time Replacement :",a)
a[0:2] = ['55', 67]
print("2nd Time Replacement:",a)

#Create list with three students, then check student name is present in that list or not, ask input from user
x = input("Enter Name - 'kiran' or 'raju' or 'mani' : ")
a = ['kiran', 'raju' , 'mani']
if x in a:
    print ("Yahoo...! your name is here")
else:
    print("Sorry name is not available in my list")

# Add items to list by using append() method , this will add item at end of list
list1 = ["Apple", "Banana", "cherry"]
list1.append("grape")
print("Here New List", list1)

# Add/Insert Element at specified position in that list by using insert() Method
list2 = ["Dell", "HP", "Apple", "Acer"]
list2.insert(1, "Sony")
print(list2)

# Remove element in that list by using remove() method
# Observations : in insert() we are using that by index position , but here direct string
# Hint : in order to remove element by using index , we can use pop() method
list3 = ["First", "Second", "Third", "Fourth"]
list3.remove("First")
print(list3)

# Remove element by using pop() method
# by default pop() method removes last element , but if we specify index , this will remove that element only
x = ["ear", "nose", "eyes", "skin", "finger"]
x.pop(2)
print(x)


"""
remove() vs pop() vs del perform similar operations , 
but
# Help : https://stackoverflow.com/questions/11520492/difference-between-del-remove-and-pop-on-lists
# Help : https://www.csestack.org/difference-between-remove-del-pop-python-list/
==> remove()   delete the matching element/object whereas del and pop removes the element at a specific index. 
==> del and pop deals with the index. 
==> The only difference between two is that- pop return deleted the value from the list and del does not return anything.
==> Pop is only way that returns the object.
==> Remove is the only one that searches object (not index).
"""


# Check given number is prime number or not
def  prime2(num):
  if num > 1:
    for i in range(2,num//2+1): # here we can use range(2,num) , num//2+1 will reduce computing time
      if (num % i) == 0:
        return "It's not prime number"
    else:
      return "it's Prime Number"
  else :
    return "It's not Prime Number"

x = int(input("i can check entered number is prime or not\n Enter your number :  "))
print(prime2(x))


# Type Conversion or Type casating
# SI Rule : String to integer or float not possible

#print prime numbers in specific range
# pending

# Reverse a given number and return true if it is the same as the original number
# Method - 1
mainnum = 121
num = mainnum
revnum = 0
while num > 0:
    remainder = num % 10
    revnum = (revnum * 10) + remainder
    num = num // 10
if mainnum == revnum:
    print("true")
else:
    print("false")

# Method - 2
x = 121
x1 = str(x)
y1 = str(x)
y2 = y1[::-1]
if x1 == y2:
    print("true")
else:
    print("false")


#Print the following pattern
'''
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
'''
x = 6
for a in range(x):
    for b in range(a):
        print(a, end = " ")
    print(" ")
    
#change-2 
update-1
