# https://www.hackerrank.com/challenges/swap-case/problem

# s1 = 'AZ'
# print(ord(s1[0]))
#
# # a = 97
# # z = 122
# #32 diff
# # A = 65
# # Z = 90
#
# print(chr(ord(s1[0])+32))

# Method- 1
sa = 'abcdefghijklmnopqrstuvwxyz'
sA = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def swap_case(s):
    s1 = ""
    for i in range(len(s)):
        if s[i].isalpha() and s[i] in sa:
            for k in range(len(sa)):
                if s[i] == sa[k]:
                    s1 = s1 + sA[k]
        elif s[i].isalpha() and s[i] in sA:
            for m in range(len(sA)):
                if s[i] == sA[m]:
                    s1 = s1 + sa[m]
        else:
            s1 = s1 + s[i]
    return s1

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

# method - 2

def swap_case(s):
    s1 = ""
    for i in range(len(s)):
        if 97 <= ord(s[i]) <= 122:
            s1 = s1 + chr(ord(s[i])-32)
        elif 65 <= ord(s[i]) <= 90:
            s1 = s1 + chr(ord(s[i])+32)
        else:
            s1 = s1 + s[i]
    return s1
Prathyusha