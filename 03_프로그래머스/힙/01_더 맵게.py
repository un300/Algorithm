import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    cnt = 0
    
    while (scoville[0] < K):
        min01 = heapq.heappop(scoville)
        min02 = heapq.heappop(scoville)
        new = min01 + (min02 * 2)
        
        heapq.heappush(scoville, new)
        cnt += 1
        
        if (not scoville):
            return -1
        elif (len(scoville) == 1) & (scoville[0] < K):
            return -1
    return cnt




