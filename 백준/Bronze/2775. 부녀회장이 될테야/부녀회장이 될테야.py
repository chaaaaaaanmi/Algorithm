t = int(input())

# 1 <= k, n <= 14
# 14호까지 있다.
dp = [[i for i in range(1, 15)]]

# dp 채우기
def fill_dp(k):

    # 층
    for i in range(len(dp), k+1):
        temp = []
        # 호
        for j in range(14):
            temp.append(sum(dp[i-1][:j+1]))
        dp.append(temp)
                

for _ in range(t):
    k = int(input())
    n = int(input())

    if k > len(dp)-1:
        fill_dp(k)
    
    print(dp[k][n-1])