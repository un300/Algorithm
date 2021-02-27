import sys
sys.setrecursionlimit(10000000)

from collections import deque

def DFS(relation, check, person, il_chon_graph) :
    global cnt
    check[person] = True

    cnt += 1
    for il_chon in relation[person] :
        if not check[il_chon] :
            il_chon_graph[il_chon] = cnt
            DFS(relation, check, il_chon, il_chon_graph
        


def solution() :
    n = int(input())
    person01, person02 = map(int, input().split())
    m = int(input())

    relation = [ [] for _ in range(n+1) ]
    check    = [False] * (n+1)
    il_chon_graph = [0] * (n+1)
    
    for _ in range(m) :
        p01, p02 = map(int, input().split())
        relation[p01].append(p02)
        relation[p02].append(p01)

    global cnt
    cnt = 0

    DFS(relation, check, person01, il_chon_graph)

    if il_chon_graph[person02] == 0:
        return -1
    else :
        return il_chon_graph[person02]


print(solution())