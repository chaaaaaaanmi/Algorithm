n, m = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]
B = [list(map(int, input().split())) for _ in range(n)]
result = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        result[i][j] = A[i][j] + B[i][j]

for r in result:
    print(*r)