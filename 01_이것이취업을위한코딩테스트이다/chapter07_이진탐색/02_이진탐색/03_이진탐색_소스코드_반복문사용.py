def binary_search(array, target):
    
    start = 0
    end   = len(array)

    mid   = (start + end) // 2

    while start < end:
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid-1
            mid = (start + end) // 2
        else :
            start = mid + 1
            mid = (start + end) // 2
    
    return None



a = [2, 5, 7, 10, 49, 60]

print(binary_search(a, target))