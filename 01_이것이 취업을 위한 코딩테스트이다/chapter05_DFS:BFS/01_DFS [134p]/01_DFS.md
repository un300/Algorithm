###### 2021-01-14

# 05-1 DFS

- DFS는 깊이 우선 탐색이라 부르며, 그래프의 깊은 부분을 우선적으로 탐색하는 알고리즘이다.
- 그래프는 **노드**, **간선**으로 표현되며, 노드는 **정점** 이라고도 말한다.
- 두 노드가 간선으로 연결되어 있으면 두 노드는 인접하다고 말할 수 있다.
- 프로그래밍에서 **그래프** 는 크게 2가지 방식으로 표현할 수 있는데 코딩 테스트에서는 두가지 방법을 모두 사용하기에 두 개념에 대해 바르게 알고 있도록 하자.
  - **인접행렬(Adjacency Matrix)** : 2차원 배열로 그래프의 연결 관계를 표현한 방식
  - **인접리스트(Adjacency List)** : 리스트로 그래프의 연결 관계를 표현하는 방식
- `스택` 구조에 기반한 알고리즘으로 재귀함수를 사용한다.



##### 인접행렬의 예

- 파이썬에서는 2차원 리스트로 구현할 수 있다

~~~python
INF = 999999999999 # 무한의 비용선언
array = [
	[0, 7, 5],
	[7, 0, INF],
	[5, INF, 0]
]
print(array)
~~~



##### 인접리스트의 예

~~~python
graph = [[] for _ in range(3)]

# 노드0에 연결된 노드정보{(노드번호, 거리)} 저장
graph[0].append((1, 7))
graph[0].append((2, 5))

# 노드1에 연결된 노드정보{(노드번호, 거라)} 저장
graph[1].append((0, 7))

# 노드2에 연결된 노드정보 {(노드번호, 거리)} 저장
graph[2].append((0, 5))

print(graph)
~~~



## 1. DFS 구현코드

~~~python
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


~~~





