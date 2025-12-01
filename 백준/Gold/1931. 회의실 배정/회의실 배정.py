n = int(input())
meetings = [tuple(map(int, input().split())) for _ in range(n)]
# 끝나는 시간 기준으로 정렬, 끝나는 시간이 같으면 시작 시간이 더 빠른게 앞
meetings.sort(key=lambda x: (x[1], x[0])) 

idx = 0
cnt = 1
finish = meetings[0][1]
while idx < (n-1):

    idx += 1

    meeting = meetings[idx]

    if finish > meeting[0]:
        continue

    finish = meeting[1]
    cnt += 1


print(cnt)