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


def solution(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]
    for r in _reserve:
        f = r - 1
        b = r + 1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    return n - len(_lost)