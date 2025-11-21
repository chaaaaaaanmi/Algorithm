n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

cnt = 0
while k != 0:

    if k == 0:
        break

    if len(coins) == 0:
        break

    coin = coins.pop()
    if coin > k:
        continue

    temp = k // coin
    cnt += temp
    k = k - (coin * temp)


print(cnt)