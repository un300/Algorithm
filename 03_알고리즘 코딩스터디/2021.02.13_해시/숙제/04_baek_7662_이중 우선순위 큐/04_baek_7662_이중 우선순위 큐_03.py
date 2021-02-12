

# I n  > n 삽입
# D 1  > 최댓값 삭제
# D -1 > 최솟값 삭제


import heapq
import sys

### (1) 클래스 구현

class dual_priority_queue :
    def __init__(self) :
        self.max_heap = []
        self.min_heap = []
        self.cnt_dict = {}

    def input_data(self, way, n):
        if way == 'I' :
            heapq.heappush(self.min_heap, n)
            heapq.heappush(self.max_heap, -n)

            if n not in self.cnt_dict.keys() :
                self.cnt_dict[n] = 1
            else :
                self.cnt_dict[n] += 1
        else :
            if not list(self.cnt_dict.keys()) :
                return True
            elif n==1 :
                while self.max_heap :
                    max_value = -heapq.heappop(self.max_heap)
                    if max_value in self.cnt_dict.keys() :
                        self.cnt_dict[max_value] -= 1
                        if self.cnt_dict[max_value] == 0 :
                            del self.cnt_dict[max_value]
                        break
            else :
                while self.min_heap :
                    min_value = heapq.heappop(self.min_heap)
                    if min_value in self.cnt_dict.keys() :
                        self.cnt_dict[min_value] -= 1
                        if self.cnt_dict[min_value] == 0 :
                            del self.cnt_dict[min_value]
                        break

#### (2) 문제해결

def solution() :

    fast_input = sys.stdin.readline
    
    T = int(fast_input().strip())
    for _ in range(T) :
        k = int(fast_input().strip())
        instance = dual_priority_queue()
        for _ in range(k) :
            way, n = fast_input().strip().split()
            n = int(n)

            instance.input_data(way, n)
        
        answer_list = sorted(instance.cnt_dict.keys())

        if not answer_list :
            print('EMPTY')
        else :
            min_answer = answer_list[0]
            max_answer = answer_list.pop()
            print('{} {}' .format(max_answer, min_answer))
            

solution()