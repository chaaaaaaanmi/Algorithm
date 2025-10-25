n = int(input())
floor = [0] * (n+1)

for i in range(1, n+1):
    floor[i] = int(input())

dp = [0] * (n+1)

if n >= 1:
    dp[1] = floor[1]

if n >= 2:
    dp[2] = floor[1] + floor[2]

if n >= 3:
    dp[3] = max((floor[1] + floor[3]), (floor[2] + floor[3]))

for i in range(4, n+1):
    dp[i] = max(
        (dp[i-2] + floor[i]),
        (dp[i-3] + floor[i-1] + floor[i])
    )

print(dp[n])