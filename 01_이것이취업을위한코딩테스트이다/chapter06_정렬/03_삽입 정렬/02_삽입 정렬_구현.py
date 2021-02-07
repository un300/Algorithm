
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)) :
    for j in range(i, 0, -1) :
        if array[j] < array[j-1] :
            array[j]. array[j-1] = array[j-1], array[j]
        else :
            break  ### 앞에서 부터 차례애로 정렬되기 때문에!

print(array)