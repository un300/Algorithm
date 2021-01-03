N = int(input())


for n in range(1, N+1):
    digit_list = list(map(int, str(n)))
    answer = n + sum(digit_list)
    if answer == N :
        result = n
        break

    if n == N:
        result = 0
        break

print(result)