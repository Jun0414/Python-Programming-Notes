# 단일 출발 단일 도착


# 단일 출발 다중 도착

# 시간 복잡도(E: 간선 수)
# 최악 O(ElogE)

# Dijkstra (다익스트라)
# 설명 : 첫 정점을 기준으로 연결되어 있는 정점들을 추가하며, 최단 거리를 갱신하는 방법 (BFS와 유사)

import heapq

# 우선순위 큐 구현 예시
# queue = []
# heapq.heappush(queue, [2, "A"])
# heapq.heappush(queue, [5, "B"])
# heapq.heappush(queue, [1, "C"])
# heapq.heappush(queue, [7, "D"])

def dijkstra(graph, start):
  # 초기화
  distances = {node: float('inf') for node in graph}
  distances[start] = 0
  queue = []
  heapq.heappush(queue, [distances[start], start])

  while queue:
    # 우선순위 큐에서 노드하나 받기
    current_distance, current_node = heapq.heappop(queue)

    # 저장된 노드의 거리보다 크다면 스킵
    if distances[current_node] < current_distance:
      continue

    # 인접한 노드와 거리 가중치 받아 반복문
    for adjacent, weight in graph[current_node].items():
      # 새로운 거리 계산 (기존 거리 + 가중치)
      distance = current_distance + weight

      # 새로운 경로가 짧다면 갱신하고 우선순위 큐에 삽입
      if distance < distances[adjacent]:
        distances[adjacent] = distance
        heapq.heappush(queue, [distance, adjacent])

  return distances

# 그래프 구현
graph = {
  'A': {'B': 8, 'C': 1, 'D': 2},
  'B': {},
  'C': {'B': 5, 'D': 2},
  'D': {'E': 3, 'F': 5},
  'E': {'F': 1},
  'F': {'A': 5}
}

result = dijkstra(graph, 'A')
print(result)

# 출력 예시
# ('A'로 부터의 최단거리)
# {'A': 0, 'B': 6, 'C': 1, 'D': 2, 'E': 5, 'F': 6}


# 다중 출발 다중 도착