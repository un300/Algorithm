

## 왜안됨?
# from collections import deque
# import sys

# def solution() :
#     fast_input = sys.stdin.readline
#     N = int(fast_input().rstrip())
#     input_list = [ int(fast_input().rstrip()) for _ in range(N) ]
#     input_list.sort()
#     queue = deque(input_list)

#     answer = 0
#     temp_sum = queue.popleft()

#     while queue :
#         most_small = queue.popleft()
#         temp_sum += most_small
#         answer += temp_sum
        
#     print(answer)



# solution()




import heapq
import sys

def solution() :
    fast_input = sys.stdin.readline
    N = int(fast_input().rstrip())
    input_list = [ int(fast_input().rstrip()) for _ in range(N) ]
    heapq.heapify(input_list)

    answer = 0

    while len(input_list) != 1 :
        num01 = heapq.heappop(input_list)
        num02 = heapq.heappop(input_list)
        heapq.heappush(input_list, num01+num02)
        answer += num01 + num02


    print(answer)

solution()