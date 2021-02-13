# N : 노드수
# M : 간선수
# V : 시작노드번호

N, M, V = map(int, input().split())

visited_DFS = [False] * (N+1)
visited_BFS = [False] * (N+1)

## 그래프정보 입력
graph = [[] for _ in range(N+1)]
for _ in range(M):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

## 그래프 정렬 (작은거부터 탐방해야 하기 때문)
for element_list in graph:
    element_list.sort()

### 1. DFS

def DFS(graph, node, visited):
    visited[node] = True
    print(node, end=' ')

    for linked_node in graph[node]:
        if not visited[linked_node] :  
            DFS(graph, linked_node, visited)



### 2. BFS
from collections import deque
def BFS(graph, node, visited):
    queue = deque([node])
    visited[node] = True

    while queue :
        current_node = queue.popleft()
        print(current_node, end=' ')

        for linked_node in graph[current_node]:
            if not visited[linked_node]:
                queue.append(linked_node)
                visited[linked_node] = True




DFS(graph, V, visited_DFS)
print('')
BFS(graph, V, visited_BFS)
