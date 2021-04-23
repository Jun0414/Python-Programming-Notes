from collections import deque

# Breadth-First Search(BFS, 너비 우선 탐색)
# 설명 : 정점들과 같은 레벨에 있는 노드들(형제노드들)을 먼저 탐색하는 방식

# 시간복잡도
# 최악 O(노드 수 + 간선 수)


def bfs(graph, start, visited):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque([start])

    # 현재 노드 방문 처리
    visited[start] = 1

    # 큐가 빌때까지
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end=' ')

        # 해당원소와 연결된, 아직 방문하지 않은 노드 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = 1

# 노드의 연결된 정보 리스트 자료형 표현(2차원 리스트)
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

# 노드의 방문 정보 저장 리스트 자료형 표현(1차원 리스트)
visited = [0] * 9

# 처음 방문할 노드
node = 1

bfs(graph, node, visited)

# 출력 예시
# 1 2 3 8 7 4 5 6
