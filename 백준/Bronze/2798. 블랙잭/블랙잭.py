N, M = map(int, input().split())
cards = list(map(int, input().split()))

def solve(idx, sum, choice):
    global max_sum

    # M을 넘으면 return
    if sum > M:
        return

    # 카드 3장 다 고르면 max_sum 갱신
    if choice == 3:
        # 갱신
        max_sum = max(max_sum, sum)
        return

    # cards의 길이를 넘으면 return
    if idx >= N:
        return

    # 해당 인덱스의 카드를 더하기
    solve(idx+1, sum+cards[idx], choice+1)
    # 해당 인덱스의 카드 건너뛰기
    solve(idx+1, sum, choice)


max_sum = 0
solve(0, 0, 0)
print(max_sum)