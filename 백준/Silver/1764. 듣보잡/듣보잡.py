import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = set()
answer = []

for _ in range(n):
    arr.add(input().strip())

for _ in range(m):
    name = input().strip()

    if name in arr:
        answer.append(name)

answer.sort()
print(len(answer))
print(*answer, sep="\n")