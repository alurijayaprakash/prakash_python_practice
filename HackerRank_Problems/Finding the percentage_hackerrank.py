n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
# print(student_marks)
# print(query_name)
for i in student_marks:
    if i == query_name:
        list1 = student_marks[i]
        # print(list1)
avg1 = sum(list1)/len(list1)
print("{:.2f}".format(avg1))