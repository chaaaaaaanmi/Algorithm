def solution(m, n, puddles):
    answer = 0
    
    # 헷갈리니까 바꿔버리기
    puddles = [[y, x] for [x, y] in puddles]
    
    dp = [[0] * (m+1) for _ in range(n+1)] # m x n
    dp[1][1] = 1 # 집
    
    for r in range(1, n+1):
        for c in range(1, m+1):
            
            # 탐색 시작점 건너 뛰기
            if r == 1 and c == 1:
                continue
                
            # 물에 잠겨 갈 수 없음
            if [r, c] in puddles:
                dp[r][c] = 0
            
            else:
                dp[r][c] = dp[r-1][c] + dp[r][c-1]
    
    return dp[n][m] % 1000000007