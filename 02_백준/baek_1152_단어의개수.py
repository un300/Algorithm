input_str = input()

if input_str == ' ':
    print(0)
else:
    answer = input_str.strip().split(' ')
    print(len(answer))