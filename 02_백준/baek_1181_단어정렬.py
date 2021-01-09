import sys

N = int(sys.stdin.readline())

array = []
for _ in range(N) :
    input_word = sys.stdin.readline().strip()
    array.append(input_word)


set_list = list(set(array))
new_array = [[len(element), element] for element in set_list ]
answer_array = sorted(new_array, key=lambda x : ( x[0], x[1] ))

print('\n'.join(answer_array))