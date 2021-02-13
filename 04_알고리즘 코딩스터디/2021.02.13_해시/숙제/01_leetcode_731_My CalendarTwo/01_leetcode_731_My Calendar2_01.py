from collections import deque
from itertools import combinations


## 시간초과
class MyCalendarTwo:
    
    def __init__(self):
        self.queue = deque([])

    def book(self, start: int, end: int):
        
        new_set = set(list(range(start, end)))

        if len(self.queue) < 2 :
            self.queue.append(new_set)
            return True
        else :
            combibation_list = list(combinations(self.queue, 2))
            bool_list = []
            for set01, set02 in combibation_list:
                bool_list.append(len(set01 & set02 & new_set))

            if sum(bool_list)>0:
                return False
            else :
                self.queue.append(new_set)
                return True
            
            


a = MyCalendarTwo()
print(a.book(10, 20))
print(a.book(50, 60))
print(a.book(10, 40))
print(a.book(5, 15))
print(a.book(5, 10))
print(a.book(25, 55))