
###################################### 시간초과
# from collections import deque
# import sys

# class Tomato :
#     def __init__(self, array) :
#         self.array     = array
#         self.queue     = deque([])
#         self.direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
#         self.day       = 0


#     def BFS(self, ripe_tomato_list) :
#         self.queue.append(ripe_tomato_list)

#         while self.queue[0] :
#             self.day += 1
#             today_tomato = self.queue.popleft()

#             next_day_tomato = []
#             for row, col in today_tomato :
#                 self.array[row][col] = 1
#                 for nr, nc in self.direction :
#                     dr = row + nr
#                     dc = col + nc

#                     if (dr>=0) & (dc>=0) & (dr<=len(self.array)-1) & (dc<=len(self.array[0])-1) :
#                         if self.array[dr][dc] == 0 :
#                             next_day_tomato.append((dr, dc))

#             self.queue.append(next_day_tomato)


#     def print_(self) :
#         for row_list in self.array :
#             for element in row_list :
#                 if element == 0 :
#                     return -1

#         return self.day-1




# def solution() :
#     fast_input = sys.stdin.readline
#     col, row = map(int, fast_input().rstrip().split())
#     array = [ list(map(int, fast_input().rstrip().split())) for _ in range(row) ]

#     ripe_tomato = []
#     for dr in range(row) :
#         for dc in range(col) :
#             if array[dr][dc] == 1 :
#                 ripe_tomato.append((dr, dc))

#     instance = Tomato(array)
#     instance.BFS(ripe_tomato)
#     print(instance.print_())

# solution()









from collections import deque
import sys


def Tomato(ripe_tomato_list, array) :
    queue = deque([ripe_tomato_list])
    direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    day = 0

    while queue[0] :
        day += 1
        today_tomato = queue.popleft()
        
        tommorow_tomato = []
        for row, col in today_tomato :
            array[row][col] = 1

            for dr, dc in direction :
                nr = row + dr
                nc = col + dc
                if (0<=nr<len(array)) & (0<=nc<len(array[0])) :
                    if array[nr][nc] == 0:
                        tommorow_tomato.append((nr, nc))
        queue.append(tommorow_tomato)

    return day - 1


def solution() :
    fast_input = sys.stdin.readline
    col, row = map(int, fast_input().rstrip().split())
    array = [ list(map(int, fast_input().rstrip().split())) for _ in range(row) ]

    ripe_tomato = []
    for dr in range(row) :
        for dc in range(col) :
            if array[dr][dc] == 1 :
                ripe_tomato.append((dr, dc))


    answer = Tomato(ripe_tomato, array)   

    for r in range(row) :
        for c in range(col) :
            if array[r][c] == 0 :
                return -1

    return answer


print(solution())
