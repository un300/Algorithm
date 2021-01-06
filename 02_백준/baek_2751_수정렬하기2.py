# 병합정렬

def merge_sort(input_list):
    if len(input_list) > 1 :
        mid_index = len(input_list) // 2

        # 리스트를 반으로 나누어 두개의 리스트로 만듬
        left_half_list  = merge_sort(input_list[ : mid_index])
        right_half_list = merge_sort(input_list[mid_index : ])

        
        # 리스트 인덱스 에러를 해결..
        standard_num = len(left_half_list) + len(right_half_list)
        left_half_list.append(float("inf"))
        right_half_list.append(float("inf"))

        # 반으로 나누는 리스트를 병합 (병합과 동시에 정렬)
        left_idx   = 0
        right_idx  = 0
        merge_list = []
        while True :
            if left_half_list[left_idx] < right_half_list[right_idx]:
                merge_list.append(left_half_list[left_idx])
                left_idx += 1
            else :
                merge_list.append(right_half_list[right_idx])
                right_idx += 1

            if standard_num == left_idx + right_idx:
                break

        return merge_list

    else :
        return input_list




N = int(input())

all_list = []
for _ in range(N):
    input_number = int(input())
    all_list.append(input_number)

answer_list = merge_sort(all_list)
for answer in answer_list:
    print(answer)