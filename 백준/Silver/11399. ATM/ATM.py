n = int(input())
people = list(map(int, input().split()))
people.sort()

time = people[0]
temp = people[0] # 대기시간
for i in range(1, n):
    time += people[i] + temp
    temp += people[i]

print(time)