
# Create Function , which calcuate sum of digits in list , x = [1,2,33,44] then output is sum of 1+2+3+3+4+4 = ?

def digitprogram2(a):
    sum = 0
    for i in a:
        j = i
        while j != 0:
            print("1st J : ", j)
            rem = j % 10
            sum = rem + sum
            print("Sum is : ", sum)
            j = j // 10
            print("2nd J :", j)
            print("Loop ENDED.................")
    return sum


list1 = []
x = int(input("Enter Your 1st Number : "))
y = int(input("Enter Your 2nd Number : "))
z = int(input("Enter Your 3rd Number : "))
list1.append(x)
list1.append(y)
list1.append(z)
print("My List is : ", list1)

y = list1
print("All Addition is : ", digitprogram2(y))
