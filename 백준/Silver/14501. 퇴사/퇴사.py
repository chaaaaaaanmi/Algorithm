import sys
input = sys.stdin.readline


def solve(day, money):

    global max_money
    
    # 근무 일수를 넘어가면 최대이익 갱신
    if day >= n:
        max_money = max(max_money, money)
        return
    
    # 상담 O: 최대 근무 일수를 넘어가지 않는 선에서
    if day + T[day] <= n:
        solve(day + T[day], money + P[day])

    # 상담 X
    solve(day + 1, money)


n = int(input())
T = []
P = []
for _ in range(n):
    d, m = map(int, input().split())
    T.append(d)
    P.append(m)

max_money = 0
solve(0, 0)

print(max_money)