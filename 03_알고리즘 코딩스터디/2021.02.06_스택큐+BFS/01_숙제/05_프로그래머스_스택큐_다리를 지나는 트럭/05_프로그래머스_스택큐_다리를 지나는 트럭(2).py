## 테스트 2번 5번 통과못함

from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge_deque  = deque([False] * (bridge_length-1))
    truck_list    = list(truck_weights)[::-1]
    
    
    new_truck = truck_list.pop()
    bridge_deque.append(new_truck)
    
    cnt = 1
    while sum(bridge_deque) :
        bridge_deque.popleft()
        if not truck_list :
            bridge_deque.append(False)
            cnt += 1
        elif sum(bridge_deque, truck_list[-1]) <= weight:
            new_truck = truck_list.pop()
            bridge_deque.append(new_truck)
            cnt += 1
        else :
            bridge_deque.append(False)
            cnt += 1
            
    return cnt