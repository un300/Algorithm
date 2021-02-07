array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

count_list = [0] * len(array)

for element in array :
    count_list[element] += 1

for element, count in enumerate(count_list) :
    for _ in range(count) :
        print(element, end=' ')