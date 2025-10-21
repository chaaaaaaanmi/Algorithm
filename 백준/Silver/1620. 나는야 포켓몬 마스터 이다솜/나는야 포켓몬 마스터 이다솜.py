import sys
input = sys.stdin.readline

n, m = map(int, input().split())
poketmon = dict()

for i in range(1, n+1):
    name = input().strip()
    poketmon[str(i)] = name
    poketmon[name] = str(i)

for _ in range(m):
    question = input().strip()
    print(poketmon[question])