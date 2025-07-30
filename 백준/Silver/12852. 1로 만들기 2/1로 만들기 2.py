x = int(input())

dp = [0] * (x+1)
dp[1] = 0
if x >= 2: dp[2] = 1
if x >= 3: dp[3] = 1

nums = [[] for _ in range(x+1)]
nums[1] = [1]
if x >= 2: nums[2] = [2, 1]
if x >= 3: nums[3] = [3, 1]

for i in range(4, x+1):

    # 1 빼보기
    dp[i] = 1 + dp[i-1]
    nums[i] = [i] + nums[i-1]

    # 3 나눠보기
    if (i % 3 == 0):
        # 더 작을 때만 갱신
        if (dp[i] > 1 + dp[i//3]):
            dp[i] = 1 + dp[i//3]
            nums[i] = [i] + nums[i//3]

    # 2 나눠보기
    if (i % 2 == 0):
        # 더 작을 때만 갱신
        if (dp[i] > 1 + dp[i//2]):
            dp[i] = 1 + dp[i//2]
            nums[i] = [i] + nums[i//2]

print(dp[x])
print(*nums[x])