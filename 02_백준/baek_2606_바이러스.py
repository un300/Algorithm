N = int(input())  # 컴퓨터수
M = int(input())  # 연결된 가지수

visited = [False] * (N+1)

graph = [[] for _ in range(N+1)]
for _ in range(M):
    node01, node02 = map(int, input().split())
    graph[node01].append(node02)
    graph[node02].append(node01)

    

def DFS(graph, node, visited):
    visited[node] = True

    for linked_node in graph[node]:
        if not visited[linked_node]:
            DFS(graph, linked_node, visited)




from collections import deque

def BFS(graph, node, visited):
    visited[node] = True
    queue = deque([node])

    while queue:
        current_node = queue.popleft()
        for linked_node in graph[current_node]:
            if not visited[linked_node]:
                visited[linked_node] = True
                queue.append(linked_node)


#####################



## 1. DFS
DFS(graph, 1, visited)
print(sum(visited)-1)

## 2. BFS
BFS(graph, 1, visited)
print(sum(visited)-1)