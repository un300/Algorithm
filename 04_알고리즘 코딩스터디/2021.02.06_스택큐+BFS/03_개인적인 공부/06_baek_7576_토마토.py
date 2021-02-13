## 아직 덜 품


from collections import deque
def BFS(x, y, array):
    queue = deque([ [(x, y)] ])
    direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    cnt = 0
    while queue[0] :
        today_mature_list = queue.popleft()
        cnt += 1
        tommorow_mature_list = []
        for x, y in today_mature_list :
            for dx, dy in direction :
                nx = x + dx
                ny = y + dy

                if (nx>=0) & (ny>=0) & (nx<=len(array[0])-1) & (ny<=len(array)-1) :
                    if array[ny][nx] == 0:
                        tommorow_mature_list.append((nx, ny))
                        array[ny][nx] = 1
        queue.append(tommorow_mature_list)
    return cnt









def solution() :
    x, y = map(int, input().split())
    
    array = []
    for _ in range(y):
        input_list = list(map(int, input().split()))
        array.append(input_list)

    tomato_location = [(_x, _y) for _y, element_list in enumerate(array) for _x, element in enumerate(element_list) if element == 1][0]

    print(BFS(_x, _y, array))
    



solution()