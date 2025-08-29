n = int(input())
arr = list(map(int, input().split()))

m = max(arr)
total = 0
for i in range(n):
    total += arr[i]/m * 100

print(total/n)