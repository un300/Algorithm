from collections import deque

def solution(print_list, location):
    print_deque = deque([(idx, element) for idx, element in enumerate(print_list)])
    print_deque.append( (-1, -1) )
    
    
    current_index = -1
    cnt = 0
    while current_index != location :
        current_value = print_deque.popleft()
        if current_value[1] < max(print_deque, key=lambda x : x[1])[1]:
            print_deque.append(current_value)
        else :
            current_index = current_value[0]
            cnt += 1

    return cnt