def DFS(graph, node, visited) :
    visited[node] = True
    
    for next_node, connected_bool in enumerate(graph[node]) :
        if (connected_bool == 1) & (not visited[next_node]) :
            DFS(graph, next_node, visited)
    


def solution(n, graph):
    visited = [False] * n
    cnt = 0
    for com_num in range(n) :
        if not visited[com_num] :
            DFS(graph, com_num, visited)
            cnt += 1
    return cnt