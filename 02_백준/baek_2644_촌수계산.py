from collections import deque

def BFS(start, relation, distance) :
    queue = deque([start])
    distance[start] = 1
    cnt = 1
    while queue :
        cnt += 1
        for _ in range(len(queue)):     ### 이 부분 다시보기! 한번에 들어온 노드들은 모두 한번에 출력해서 봐야함
            current = queue.popleft()
            for linked in relation[current] :
                if not distance[linked] :
                    queue.append(linked)
                    distance[linked] = cnt


def solution() :
    n = int(input())
    p01, p02 = map(int, input().split())
    m = int(input())

    relation = [[] for _ in range(n+1)]
    distance = [False] * (n+1)

    for _ in range(m) :
        x, y = map(int, input().split())   
        relation[x].append(y)
        relation[y].append(x)

    BFS(p01, relation, distance)

    print(distance[p02]-1)

solution()