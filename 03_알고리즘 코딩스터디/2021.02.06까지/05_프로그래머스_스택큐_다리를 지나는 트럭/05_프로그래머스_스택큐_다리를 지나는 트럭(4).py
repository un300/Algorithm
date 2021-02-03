from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque([False] * bridge_length)
    truck  = deque([element for element in truck_weights])
    
    current_weight = 0
    
    
    flag = True
    cnt = 0
    while flag :
        cnt += 1
        crossed_truck = bridge.popleft()
        current_weight -= crossed_truck 
        if not truck :
            bridge.append(False)
        elif current_weight + truck[0] <= weight:
            start_cross_truck = truck.popleft()
            bridge.append(start_cross_truck)
            current_weight += start_cross_truck
        else :
            bridge.append(False)
        flag = current_weight
    
    return cnt