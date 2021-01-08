N = int(input())

location_array = []
for _ in range(N) :
    x, y = map(int, input().split())
    location_array.append([x, y])

answer_array = sorted(location_array, key=lambda x : (x[1], x[0]))

for answer in answer_array :
    x, y = answer
    print(x, y)
