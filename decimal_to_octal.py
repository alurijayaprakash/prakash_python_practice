
# Decimal to Octal Function , which can accept user input of Decimal number & no of digits in fractional part
'''
Here this program devided as 3 parts
main part(actual number) , left part(integer part) , right part(fractional part)
main part = leftpart + rightpart
you need to call mainpart.
for more details , please refer : https://www.youtube.com/watch?v=v0VSL1iRK_g
or know decimal to octal conversion procedure
online tool for cross reference : https://www.rapidtables.com/convert/number/decimal-to-octal.html
'''
def main1(x,f):
    # Main Program , x1 will load integer part, x2 will load fractional part of given number
    x1 = int(x)
    x2 = x - int(x)
    leftpart = left1(x1)
    rightpart = right1(x2)
    addpart = leftpart + rightpart
    return addpart


def left1(x1):
    # here is integer part , eg: x1 = 275
    newrem = 0
    pow = 1
    while x1 > 0:
        num = x1 // 8
        rem = x1 % 8
        newrem = (pow * rem) + newrem
        x1 = num
        pow = pow * 10
    return newrem


def right1(x2):
    # x2 will take fractional part only, eg: 0.4
    pow2 = 0.1
    num1 = x2
    newsol = 0
    for i in range(f):
        temp = num1 * 8
        sol = int(temp)
        newsol = (pow2 * sol) + newsol
        pow2 = pow2 * 1 / 10
        num1 = temp - sol
    return (round(newsol, 3))


x = float(input("Enter your Decimal Number : "))
f = int(input("How may number of digits do you need in fractional part, [example 0 or 1 or 2 ....] : "))

print("Octal Value of Given Number is :", main1(x,f))



# ++++++++++++++++++++++++++ Practice Data , please ignore below code ++++++++++++++++++++++++++++

# # this is Decimal to Octal program - practice code, please check non commented code in this file

# x = 275.4
# x1 = int(x)
# x2 = x - int(x)
# # here x1 = 275 , x2 = 0.4
# newrem = 0
# pow = 1
# while x1 > 0:
#     num = x1 // 8
#     rem = x1 % 8
#     newrem = (pow*rem)+newrem
#     x1 = num
#     pow = pow * 10
# print(newrem)
#
# # x2 = 0.4
# pow2 = 0.1
# num1 = x2
# newsol = 0
# for i in range(3):
#     temp = num1 * 8
#     sol = int(temp)
#     newsol = (pow2 * sol) + newsol
#     pow2 = pow2 * 1/10
#     num1 = temp - sol
#
# print(round(newsol,3))
# add2 = newrem+newsol
# print(add2)

# ++++++++++++++++++++++++++ Practice Data , please ignore above code ++++++++++++++++++++++++++++