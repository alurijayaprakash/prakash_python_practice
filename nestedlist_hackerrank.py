# https://www.hackerrank.com/challenges/nested-list/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
list1 = []
num = int(input())
for i in range(num):
    name = input().strip()
    for j in range(1):
        grade = float(input().strip())
        a = [name,grade]
        list1.append(a)
# print(list1)
mygradesdata = [grade for name,grade in list1]
mygradesdata.sort()
firstlow = mygradesdata[0]
for i in mygradesdata:
    if firstlow == i:
        continue
    else:
        secondlow = i
        break

# print(mygradesdata)
# print(secondlow)

secondlownames = [name for name,grade in list1 if grade == secondlow]
# print(secondlownames)
secondlownames.sort()
for i in secondlownames:
    print(i)