import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    cnt = 0
    
    while scoville[0] < K :
        min01 = heapq.heappop(scoville)
        min02 = heapq.heappop(scoville)
        new = min01 + (min02 * 2)
        
        if new == 0:
            return -1
        
        heapq.heappush(scoville, new)
        cnt += 1
        
        if len(scoville) < 2:
            break
    return cnt




