import sys
input = sys.stdin.readline

def add(num):
    S.add(num)

def remove(num):
    S.discard(num)

def check(num):
    if num in S:
        print(1)
    else:
        print(0)

def toggle(num):
    if num in S:
        S.discard(num)
    else:
        S.add(num)

def all():
    global S
    S = set(range(1, 21))

def empty():
    S.clear()


m = int(input())
S = set()

for _ in range(m):
    temp = input().split()
    how = temp[0]
    if len(temp) > 1:
        num = int(temp[1])

    if how == "add":
        add(num)

    elif how == "remove":
        remove(num)

    elif how == "check":
        check(num)

    elif how == "toggle":
        toggle(num)

    elif how == "all":
        all()

    elif how == "empty":
        empty()