N = int(input())

array = []
for _ in range(N):
    name, score = input().split()
    array.append( (name, int(score)) )

answer = sorted(array, key=lambda x : x[1])

for element in answer :
    print(element[0], end=' ')
