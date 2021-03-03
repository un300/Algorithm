# ## 메모리초과 : python3, pypy3
# from collections import deque
# def BFS(start, map_, N) :
#     global land
#     direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

#     queue = deque([start])
#     map_[start[0]][start[1]] = land

#     while queue :
#         row, col = queue.popleft()

#         for dr, dc in direction :
#             nr = row + dr
#             nc = col + dc
#             if (0<=nr<N) & (0<=nc<N) :
#                 if map_[nr][nc] == 1:
#                     queue.append((nr, nc))
#                     map_[nr][nc] = land
    

# def find_land_location(map_, N) :
#     global land
#     land_list = [[] for _ in range(-land)]

#     for land_num in range(-1, land-1, -1) :
#         for row in range(N) :
#             for col in range(N) :
#                 if map_[row][col] == land_num :
#                     land_list[-land_num-1].append((row, col))

#     return land_list


# from itertools import combinations, product
# import heapq
# def find_distance(land_location) :
#     answer = []
#     for select_two_land in list(combinations(land_location, 2)) :
#         for point01, point02 in list(product(*select_two_land)) :
#             distance = abs(point01[0]-point02[0])+abs(point01[1]-point02[1])
#             heapq.heappush(answer, distance)
#     return heapq.heappop(answer)-1


# def solution() :
#     N = int(input())
#     map_ = [ list(map(int, input().split())) for _ in range(N) ]

#     global land
#     land = 0
#     for row in range(N) :
#         for col in range(N) :
#             if map_[row][col] == 1:
#                 land -= 1
#                 BFS((row, col), map_, N)

#     land_location = find_land_location(map_, N)
#     answer = find_distance(land_location)

#     print(answer)

# solution()





############################################################################################






from collections import deque
def BFS(start, map_, N) :
    global land
    global beach
    global beach_label

    direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    queue = deque([start])
    map_[start[0]][start[1]] = land

    while queue :
        row, col = queue.popleft()

        for dr, dc in direction :
            nr = row + dr
            nc = col + dc
            if (0<=nr<N) & (0<=nc<N) :
                if map_[nr][nc] == 1 :
                    queue.append((nr, nc))
                    map_[nr][nc] = land
                elif map_[nr][nc] == 0 :
                    beach.append((row, col))
                    beach_label.append(map_[row][col])
    

def extension(map_, N) :
    global beach
    global beach_label

    direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    loop = 1
    while beach :
        for _ in range(len(beach)):

            land_set = set(beach_label)
            r, c = beach.popleft()
            beach_label.popleft()

            for dr, dc in direction :
                nr = r + dr
                nc = c + dc
                if (0<=nr<N) & (0<=nc<N) :
                    if map_[nr][nc] == 0 :
                        map_[nr][nc] = map_[r][c]
                        beach.append((nr, nc))
                        beach_label.append(map_[r][c])
                    elif (map_[r][c] != map_[nr][nc]) & (len(land_set)!=1) :
                        return 2*loop-1
                    elif (map_[r][c] != map_[nr][nc]) :
                        return 2*loop
        loop += 1

def solution() :
    N = int(input())
    map_ = [ list(map(int, input().split())) for _ in range(N) ]

    global land
    global beach
    global beach_label
    land = 0
    beach = deque([])
    beach_label = deque([])
    for row in range(N) :
        for col in range(N) :
            if map_[row][col] == 1 :
                land -= 1
                BFS((row, col), map_, N)

    answer = extension(map_, N)

    print(answer)



solution()