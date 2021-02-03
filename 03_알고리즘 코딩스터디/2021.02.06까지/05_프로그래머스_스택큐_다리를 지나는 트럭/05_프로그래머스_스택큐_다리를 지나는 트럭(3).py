from collections import deque
from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque([False] * bridge_length)
    truck  = deque([element for element in truck_weights])
    
    flag = True
    cnt = 0
    while flag :
        cnt += 1
        bridge.popleft()
        if not truck :
            bridge.append(False)
        elif sum(bridge, truck[0]) <= weight:
            bridge.append(truck.popleft())
        else :
            bridge.append(False)
        flag = sum(bridge) != 0
    
    return cnt


    ## 2, 5 시간초과