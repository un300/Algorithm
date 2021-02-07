def quick_sort(array) :

    if len(array) <= 1 :
        return array

    pivot_element = array[0]
    rest_array = array[1:]

    left_array  = [ small_element for small_element in rest_array if small_element <= pivot_element ]
    right_array = [ big_element for big_element in rest_array if big_element > pivot_element ]
    sorted_array = quick_sort(left_array) + [pivot_element] + quick_sort(right_array)

    return sorted_array




a = [1, 0, 3, 4, 5, 6, 2, 7, 8, 9]


print(quick_sort(a))