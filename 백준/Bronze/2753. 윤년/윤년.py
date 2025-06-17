def solve(n):
    
    if n % 4 == 0 and n % 100 != 0:
        return 1
    
    if n % 400 == 0:
        return 1

    return 0


a = int(input())
print(solve(a))