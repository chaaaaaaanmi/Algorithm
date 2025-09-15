import sys
input = sys.stdin.readline

n = int(input())
arr_N = list(map(int, input().split()))
arr_N.sort()

m = int(input())
arr_M = list(map(int, input().split()))

for i in arr_M:

    found = False
    start = 0
    end = n-1

    while start <= end:
        mid = (start + end) // 2

        if arr_N[mid] == i:
            found = True
            print(1)
            break

        elif arr_N[mid] < i:
            start = mid + 1

        else:
            end = mid - 1

    if not found:
        print(0)