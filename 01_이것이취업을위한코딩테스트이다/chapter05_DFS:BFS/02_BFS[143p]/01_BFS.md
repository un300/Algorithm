###### 2021-01-14

# 05-2 BFS

- BFS는 너비우선탐색이라는 의미를 가진다.
- 쉽게 말해 `가까운 노드부터 탐색하는 알고리즘` 이다.
- **스택** 을 사용하는 DFS와는 달리 BFS는 **큐** 를 사용한다.
  - `collections`패키지의 `deque` 함수를 사용한다.
- 알고리즘의 작동 방식은 다음과 같다.
  1. 탐색 시작 노드를 큐에 삽입하고 방문 처리한다.
  2. 큐에서 노드를 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입한다.
  3. 2번의 과정을 더 이상 수행할 수 없을 때까지 반복한다.



## 1. BFS구현코드

```python
from collections import deque

# BFS 함수 정의

def BFS(graph, start_node, visited_marking_list) :
    # 큐를 구현하기 위해 deque함수 사용
    queue = deque([start_node])
    # 현재 탐색 중인 노드를 방문처리 한다.
    visited_marking_list[start_node] = True

    while queue :
        # 큐에서 하나의 원소를 뽑아 출력
        current_node = queue.popleft()
        print(current_node, end=' ')

        for linked_node in graph[current_node] :
            if not visited_marking_list[linked_node] :
                queue.append(linked_node)
                visited_marking_list[linked_node] = True





# 노드의 연결상태를 나타내는 그래프를 배열형태로 선언
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 방문기록 리스트 만들어주기
visited_marking_list = [False] * len(graph)

# 실행
BFS(graph, 1, visited_marking_list)
```





