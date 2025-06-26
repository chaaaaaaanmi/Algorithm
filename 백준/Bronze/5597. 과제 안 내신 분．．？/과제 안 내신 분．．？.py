students = list(range(1, 31))
arr = [int(input()) for _ in range(28)]

for i in arr:
    if i in students:
        students.pop(students.index(i))

if students[0] > students[1]:
    print(students[1])
    print(students[0])
else:
    print(students[0])
    print(students[1])