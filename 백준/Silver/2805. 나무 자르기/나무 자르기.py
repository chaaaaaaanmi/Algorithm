import sys
input = sys.stdin.readline

n, m = map(int, input().split())
trees = list(map(int, input().split()))

start = 0
end = max(trees)
max_height = 0  # 절단기 최대 높이

while start <= end:

    # 절단기 높이
    mid = (start + end) // 2

    # 가져갈 나무 길이
    length = 0
    for tree in trees:
        if tree > mid:
            length += tree - mid

    if length >= m:
        start = mid + 1
        max_height = mid
    else:
        end = mid - 1


print(max_height)