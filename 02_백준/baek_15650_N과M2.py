import itertools

N, M = map(int, input().split())

input_list = list(range(1, N+1))
answer_list = sorted(itertools.combinations(input_list, M))

for element in answer_list :
    print(' '.join(map(str, element)))



