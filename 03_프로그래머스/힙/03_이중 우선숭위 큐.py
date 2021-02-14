import heapq

class DualPriorityQueue :
    
    def __init__(self) :
        self.max_heap = []
        self.min_heap = []
        self.cnt_dict = {}

    def go(self, way, n) :
        if way=='I' :            
            heapq.heappush(self.max_heap, -n)
            heapq.heappush(self.min_heap, n)

            if n not in self.cnt_dict.keys() :
                self.cnt_dict[n] = 1
            else :
                self.cnt_dict[n] += 1
        
        elif n==1 :
            while self.max_heap :
                max_value = -heapq.heappop(self.max_heap)
                if (max_value in self.cnt_dict.keys()) :
                    self.cnt_dict[max_value] -= 1
                    if self.cnt_dict[max_value]==0 :
                        del self.cnt_dict[max_value]
                    break
        else :
            while self.min_heap :
                min_value = heapq.heappop(self.min_heap)
                if (min_value in self.cnt_dict.keys()) :
                    self.cnt_dict[min_value] -= 1
                    if self.cnt_dict[min_value]==0 :
                        del self.cnt_dict[min_value]
                    break

    def print_(self) :
        if self.cnt_dict.keys() :
            max_v = max(self.cnt_dict.keys())
            min_v = min(self.cnt_dict.keys())
            return [max_v, min_v]
        else :
            return [0, 0]



def solution(operations):
    instance = DualPriorityQueue()
    for element in operations :
        way, n = element.split()
        n = int(n)
        instance.go(way, n)

    answer = instance.print_()
    
    return answer