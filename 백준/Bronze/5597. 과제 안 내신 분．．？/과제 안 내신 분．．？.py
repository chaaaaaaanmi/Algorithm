students = set(range(1, 31))
submit = set([int(input()) for _ in range(28)])

result = sorted(students - submit)
print(result[0])
print(result[1])