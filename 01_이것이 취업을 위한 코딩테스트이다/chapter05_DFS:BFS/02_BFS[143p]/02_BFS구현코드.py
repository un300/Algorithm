from collections import deque

# BFS 함수 정의

def BFS(graph, start_node, visited_marking_list) :
    # 큐를 구현하기 위해 deque함수 사용
    queue = deque([start_node])
    # 현재 탐색 중인 노드를 방문처리 한다.
    visited_marking_list[start_node] = True

    while queue :
        # 큐에서 하나의 원소를 뽑아 출력
        current_node = queue.popleft()
        print(current_node, end=' ')

        for linked_node in graph[current_node] :
            if not visited_marking_list[linked_node] :
                queue.append(linked_node)
                visited_marking_list[linked_node] = True





# 노드의 연결상태를 나타내는 그래프를 배열형태로 선언
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 방문기록 리스트 만들어주기
visited_marking_list = [False] * len(graph)

# 실행
BFS(graph, 1, visited_marking_list)