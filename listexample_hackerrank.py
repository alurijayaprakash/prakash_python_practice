# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
n = int(input())
arr = list(map(int, input().split()))
arr.sort(reverse=True)
num = arr[0]
for i in arr:
    if i == num:
        continue
    else:
        print(i)
        break
