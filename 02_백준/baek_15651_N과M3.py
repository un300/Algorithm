import itertools

N, M = map(int, input().split())

input_list = list(range(1, N+1))
array = []
for _ in range(M) :
    array.append(input_list)


answer = sorted(itertools.product(*array))
print(answer)

