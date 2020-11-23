# https://www.hackerrank.com/challenges/string-validators/problem

#Method-1

if __name__ == '__main__':
    mystring = input()

    print(any(s.isalnum() for s in mystring))

    print(any(s.isalpha() for s in mystring))

    print(any(s.isdigit() for s in mystring))

    print(any(s.islower() for s in mystring))

    print(any(s.isupper() for s in mystring))


'''
any() function
The any() function returns True if any element of an iterable is True. If not, any() returns False.
https://www.programiz.com/python-programming/methods/built-in/any
'''
