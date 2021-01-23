# 이진탐색 구현
def binary_search(array, target):
    start = 0
    end   = len(array)

    while start < end :
        mid = (start + end) // 2
        if array[mid] == target :
            return True
        elif array[mid] > target:
            end = mid-1
        else :
            start = mid + 1

    return False

# 입력
N = int(input())
product_number_list = list(map(int, input().split()))
M = int(input())
find_number_list = list(map(int, input().split()))

# 이진탐색을 적용하기 위해 정렬
sorted_product_number_list = sorted(product_number_list)

# 출력
answer = ['yes' if binary_search(sorted_product_number_list, element) else 'no' for element in find_number_list]
print(answer)
