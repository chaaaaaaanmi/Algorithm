n = int(input())

if n == 1:
    print(1)

else:

    min = 2
    max = 7
    count = 1
    answer = 2

    while True:
        if min <= n <= max:
            print(answer)
            break

        else:
            min += 6 * count
            max += 6 * (count + 1)
            count += 1
            answer += 1