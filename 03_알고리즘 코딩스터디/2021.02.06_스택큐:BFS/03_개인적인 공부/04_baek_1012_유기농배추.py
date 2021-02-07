
# 1. DFS

def DFS(x, y, array, visited):
    if (x<0) | (y<0) | (x>len(array[0])) | (y>len(array)) :
        return False
    elif (visited[x][y]) | (array[x][y]==0) :
        return False
    else :
        visited[x][y] = True
        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for dx, dy in direction :
            new_x = x + dx
            new_y = y + dy
            DFS(new_x, new_y, array, visited)

        return True



# 2. 해결
def solution():
    ## 입력
    T = int(input())
    for _ in range(T):
        row, col, cnt = map(int, input().split())
        array   = [[0]*col for _ in range(row)]
        visited = [[False]*col for _ in range(row)]
        for _ in range(cnt):
            x, y = map(int, input().split())
            array[x][y] = 1

        answer_list = []
        for x in range(row) :
            for y in range(col) :
                answer = DFS(x, y, array, visited)
                answer_list.append(answer)
        print(sum(answer_list))

solution()