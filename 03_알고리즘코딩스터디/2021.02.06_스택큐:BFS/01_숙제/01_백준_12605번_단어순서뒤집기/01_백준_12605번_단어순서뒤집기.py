N = int(input())

for i in range(N):
    input_string_list = input().split(' ')
    answer = ' '.join(input_string_list[::-1])
    print('Case #{}: {}' .format(i+1, answer))