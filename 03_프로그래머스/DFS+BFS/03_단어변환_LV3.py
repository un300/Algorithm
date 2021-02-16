from collections import deque

## 두 딘어의 같은 알파벳 수를 세어줌
def match(word01, word02) :
    match_list = []
    for i in range(len(word01)) :
        temp = word01[i] == word02[i]
        match_list.append(temp)
    return sum(match_list)


def BFS(graph, visited, node):
    queue = deque([node])
    visited[node] = 0
    
    while queue :
        current_node = queue.popleft()
        for next_node in graph[current_node] :
            if not visited[next_node] :
                visited[next_node] = visited[current_node] + 1
                queue.append(next_node)
                        



def solution(begin, target, words):
    if target not in words :
        return 0
    
    queue = deque(words)
    queue.appendleft(begin)
    
    # 단어사이의 그래프를 만들어줌
    graph   = [[] for _ in range(len(queue))]
    visited = [False] * len(queue)
    for idx01, node in enumerate(queue) :
        for idx02, connected_node in enumerate(queue) :
            if match(node, connected_node) == len(begin)-1 :
                graph[idx01].append(idx02)
                

    # 위에서 만든 그래프로 BFS시작
    BFS(graph, visited, 0)
    
    index = queue.index(target)
    return visited[index]
    