import sys
limit_number = 15000
sys.setrecursionlimit(limit_number)



def DFS(node, graph, visited) :
    visited[node] = True
    for linked_node in graph[node] :
        if not visited[linked_node] :
            DFS(linked_node, graph, visited)


def solution() :
    fast_input = sys.stdin.readline
    N, M = map(int, fast_input().rstrip().split())

    graph   = [[] for _ in range(N+1)]
    visited = [False] * (N+1)
    for _ in range(M) :
        node01, node02 = map(int, fast_input().rstrip().split())
        graph[node01].append(node02)
        graph[node02].append(node01)

    cnt = 0
    for node in range(1, N+1) :
        if not visited[node] :
            DFS(node, graph, visited)
            cnt += 1
    print(cnt)



solution()