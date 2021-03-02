from collections import deque

def BFS(graph, visited) :
    queue = deque(['INC'])
    

    


def solution(tickets) :
    graph = {}
    visited = {}

    for start, end in tickets :
        if start not in graph.keys() :
            graph[start] = [end]
            visited[start] = []
        else :
            graph[start].append(end)
    
