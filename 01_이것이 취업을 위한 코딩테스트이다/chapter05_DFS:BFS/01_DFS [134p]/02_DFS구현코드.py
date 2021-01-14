#### 깊이 우선 탐색(DFS)

# DFS 함수정의
def DFS(graph, node, visited_marking_list) :
    visited_marking_list[node] = True

    print(node, end=' ')
    for linked_node in graph[node] :
        if not visited_marking_list[linked_node] :
            DFS(graph, linked_node, visited_marking_list)


# 탐색할 그래프 선언
graph = [
    [],     # 'graph'라는 배열의 인댁스 자체가 노드를 뜻한다.
            # 노드번호는 1로 시작하기 때문에
            # 'graph'라는 배열의 인덱스0은 의도적으로 비워둔다.
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]


# 노드를 탐색했다는 체크리스트를 만든다.
visited_marking_list = [False] * len(graph)


# 실행!
DFS(graph, 1, visited_marking_list)

