from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge_deque  = deque([False] * (bridge_length-1))
    truck_deque   = deque(truck_weights)
    
    
    new_truck = truck_deque.popleft()
    truck_deque.append(False)
    bridge_deque.append(new_truck)
    
    cnt = 1
    while sum(bridge_deque) :
        bridge_deque.popleft()
        if sum(bridge_deque, truck_deque[0]) <= weight:
            new_truck = truck_deque.popleft()
            truck_deque.append(False)
            bridge_deque.append(new_truck)
            cnt += 1
        else :
            bridge_deque.append(False)
            cnt += 1
            
    return cnt

    ## 시간초과!
    ## 테스트 2, 5, 6 통과못함