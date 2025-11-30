def solve(n, r, c):

    if n == 0:
        return 0
    
    half = 2 ** (n-1)
    size = half * half # 한 사분면 크기

    # 어느 사분면에 해당하는지
    if r < half and c < half:
        return solve(n-1, r, c)
    elif r < half and c >= half:
        return size + solve(n-1, r, c-half)
    elif r >= half and c < half:
        return size*2 + solve(n-1, r-half, c)
    else:
        return size*3 + solve(n-1, r-half, c-half)
    
n, r, c = map(int, input().split())
print(solve(n, r, c))