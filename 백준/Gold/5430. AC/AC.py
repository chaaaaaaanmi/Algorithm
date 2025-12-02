from collections import deque
import sys
input = sys.stdin.readline

def solve(function, arr):

    arr = deque(arr)
    reverse = False

    for f in function:
        if f == "R":
            reverse = not reverse
        elif f == "D":
            if arr:
                if reverse:
                    arr.pop()
                else:
                    arr.popleft()
            else:
                return "error"

    # reverse = True 면 출력하기 전에 뒤집어주기
    if reverse:
        arr.reverse()

    return "[" + ",".join(map(str, arr)) + "]"


t = int(input())
for _ in range(t):

    # 수행할 함수
    p = input().strip()
    # 배열에 들어있는 수의 개수
    n = int(input())
    # 배열
    temp = input().strip()
    if n == 0:
        arr = []
    else:
        arr = list(map(int, temp[1:-1].split(",")))

    print(solve(p, arr))