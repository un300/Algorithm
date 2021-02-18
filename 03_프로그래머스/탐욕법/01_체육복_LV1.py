def solution(n, lost, reserve):
    possible = n-len(lost)
    
    for lost_person in lost :
        reserve_possible_list = [lost_person, lost_person-1, lost_person+1]
        for element in reserve_possible_list :
            if element in reserve :
                possible += 1
                reserve.remove(element)
                break
                
    return possible