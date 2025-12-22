n = int(input())
rgb = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * 3 for _ in range(n)]
dp[0] = rgb[0]
for i in range(1, n):
    # i번째 집 색칠하기
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + rgb[i][0] # R
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + rgb[i][1] # G
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + rgb[i][2] # B

print(min(dp[-1]))