from itertools import combinations

### 시간 초과
class MyCalendarTwo:
    
    def __init__(self):
        self.all_list = []

    def book(self, start: int, end: int):
        new_set = set(range(start, end))

        if len(self.all_list) < 2 :
            self.all_list.append(new_set)
            return True
        else :
            combinations_list = list(combinations(self.all_list, 2))
            bool_list = list(map(lambda x : len(x[0] & x[1] & new_set) , combinations_list))

            if sum(bool_list) > 0:
                return False 
            else :
                self.all_list.append(new_set)
                return True


MyCalendar = MyCalendarTwo()
print(MyCalendar.book(10, 20))
print(MyCalendar.book(50, 60))
print(MyCalendar.book(10, 40))
print(MyCalendar.book(5, 15))
print(MyCalendar.book(5, 10))
print(MyCalendar.book(25, 55))