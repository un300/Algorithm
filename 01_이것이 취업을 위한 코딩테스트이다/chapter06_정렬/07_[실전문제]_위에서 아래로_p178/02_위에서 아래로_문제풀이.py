N = int(input())


array = []
for _ in range(N):
    input_element = int(input())
    array.append(input_element)

answer_list = sorted(array, reverse=True)

print(' '.join(map(str, answer_list)))