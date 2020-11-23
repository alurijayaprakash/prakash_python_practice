# https://www.hackerrank.com/challenges/python-lists/problem
list1 = []
n = int(input())
# s = input().split(" ")
for i in range(n):
    s = input().split(" ")
    if s[0] == 'insert':
        list1.insert(int(s[1]), int(s[2]))
    elif s[0] == 'append':
        list1.append(int(s[1]))
    elif s[0] == 'sort':
        list1.sort()
    elif s[0] == 'pop':
        list1.pop()
    elif s[0] == 'reverse':
        list1.reverse()
    elif s[0] == 'remove':
        list1.remove(int(s[1]))
    elif s[0] == 'print':
        print(list1)