

# 함수정의
def DFS(i, j, array, check_array, N, M) :
    # 재귀함수로 호출하기에 인데스가 벗어난 경우 함수를 중지한다.
    if ( i<0 ) | ( i>N-1 ) | ( j<0 ) | ( j>M-1 ) :
        return False
    # 현재 탐색하는 원소가 '칸막이가아님'(0)인 경우와 방문한적없는(False)인경우
    # 현재 탐색하는 원소의 상하좌우를 살핀다.
    if (array[i][j] == '0') & (not check_array[i][j]):
        check_array[i][j] = True
        DFS(i-1, j, array, check_array, N, M)
        DFS(i+1, j, array, check_array, N, M)
        DFS(i, j-1, array, check_array, N, M)
        DFS(i, j+1, array, check_array, N, M)
        return True

    return False

# 입력받는 곳
N, M = map(int, input().split())


graph = []
visited_check_array = []
for _ in range(N) :
    input_list = list(input())
    graph.append(input_list)
    visited_check_array.append( [False] * M )



# 칸막이가 아닌 원소이면서(1이 아닌 0이면서) 방문한적 없는 원소인 경우를 시작원소로 지정하여 탐색
cnt = 0
for row in range(N):
    for col in range(M):
        if ( graph[row][col] == '0' ) & ( not visited_check_array[row][col] ) :
            DFS(row, col, graph, visited_check_array, N, M)
            cnt += 1

print(cnt)