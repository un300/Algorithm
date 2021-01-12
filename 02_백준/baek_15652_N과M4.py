import itertools

N, M = map(int, input().split())

input_list = list(range(1, N+1))
answer = sorted(list(itertools.combinations_with_replacement(input_list, M)))

for element in answer :
    print(' '.join(map(str, element)))
