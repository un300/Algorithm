import itertools

N, M = map(int, input().split())
num_list = list(range(1, N+1))
answer = sorted(itertools.permutations(num_list, M))

for element in answer :
    print(' '.join(map(str, element)))


