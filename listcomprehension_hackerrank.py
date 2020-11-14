# https://www.hackerrank.com/challenges/list-comprehensions/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
x = int(input())
y = int(input())
z = int(input())
n = int(input())
print([[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n])
# list0 = []
# list1 = []
# for i in range(x+1):
#     for j in range(y+1):
#         for k in range(z+1):
#             a = [i,j,k]
#             list0.append(a)
#             if sum(a) != n:
#                 list1.append(a)
# print(list0)
# print(list1)

