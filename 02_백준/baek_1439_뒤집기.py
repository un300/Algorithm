
def solution():
    S = list(input())
    count_one = 0
    count_zero = 0
    if S[0] == '0':
        count_zero += 1
    else:
        count_one += 1

    for idx in range(len(S)-1):
        if S[idx] != S[idx + 1]:
            if S[idx + 1] == '1':
                count_one += 1
            else:
                count_zero += 1

    if count_one > count_zero:
        print(count_zero)
    else:
        print(count_one)

solution()
