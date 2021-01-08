N = int(input())

location_array = []
for _ in range(N) :
    x, y = map(int, input().split())
    location_array.append([x, y])


answer_list = sorted(location_array)


for element in answer_list :
    x, y = element
    print(x, y)