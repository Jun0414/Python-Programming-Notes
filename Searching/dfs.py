
# Depth-First Search(DFS, 깊이 우선 탐색)
# 설명 : 정점의 자식들을 먼저 탐색하는 방식

# 시간복잡도
# 최악 O(노드 수 + 간선 수)

def dfs(graph, v, visited):
    # 현재 노드 방문처리
    visited[v] = 1
    print(v, end=' ')

    # 현재 노드와 연결된 다른 노드를 재귀적 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
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

# 노드의 방문된 정보 저장 리스트 자료형(1차원 리스트)
visited = [0] * 9

# 처음 방문할 노드
node = 1

dfs(graph, node, visited)

# 출력 예시
# 1 2 7 6 8 3 4 5
