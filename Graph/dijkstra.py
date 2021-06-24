
# Dijkstra (다익스트라)
# 설명 : 첫 정점을 기준으로 연결되어 있는 정점들을 추가하며, 최단 거리를 갱신하는 방법 (BFS와 유사)
#       단일 출발 다중 도착


# 시간 복잡도(N: 노드 수, E: 간선 수)
# 최악 O(NlogE)

import sys, heapq
r = sys.stdin.readline



# List 구현(노드가 숫자인 경우 편함)

def list_dijkstra(graph, start):
  # 우선순위 큐 생성
  # 노드 개수만큼 거리 inf 초기화 및 생성
  # 첫 노드 거리 0 설정
  # 첫 노드 우선순위 큐에 삽입 (거리, 노드)
  heap_data = []
  distances = [float('inf') for _ in range(len(graph))]
  distances[start] = 0
  heapq.heappush(heap_data, (distances[start], start))

  while heap_data:
    # 우선순위 큐에서 거리, 노드 가져오기
    current_distance, current_node = heapq.heappop(heap_data)
    
    # 저장된 거리보다 비용이 많이 드는 경우
    if distances[current_node] < current_distance:
      continue
    
    # 저장된 거리보다 비용이 적게 드는 경우
    for adjacent, weight in graph[current_node]:
      # 새로운 거리 계산
      new_distance = weight + current_distance

      # 인접한 노드 저장 거리보다 비용이 적게 드는 경우
      if distances[adjacent] > new_distance:
        # 거리 갱신
        # 우선순위 큐에 추가
        distances[adjacent] = new_distance
        heapq.heappush(heap_data, (new_distance, adjacent))
  
  return distances

# 시작 번호
# 노드 수, 간선 입력 받을 개수
s = 1
n, m = map(int, r().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
  start, end, weight = map(int, r().split())
  graph[start].append((end, weight))

print('그래프: ', graph)
result = list_dijkstra(graph, s)
print('최단거리: ', result)







# Dict 구현(노드가 문자인 경우 편함)

def dict_dijkstra(graph, start):
  # 우선순위 큐 생성
  # 노드 개수만큼 거리 inf 초기화 및 생성
  # 첫 노드 거리 0 설정
  # 첫 노드 우선순위 큐에 삽입 (거리, 노드)
  heap_data = []
  distances = {node: float('inf') for node in graph}
  distances[start] = 0
  heapq.heappush(heap_data, (distances[start], start))

  while heap_data:
    # 우선순위 큐에서 거리, 노드 가져오기
    current_distance, current_node = heapq.heappop(heap_data)

    # 저장된 거리보다 비용이 많이 드는 경우
    if distances[current_node] < current_distance:
      continue

    # 저장된 거리보다 비용이 적게 드는 경우
    for adjacent, weight in graph[current_node].items():
      # 새로운 거리 계산
      new_distance = weight + current_distance

      # 인접한 노드 저장 거리보다 비용이 적게 드는 경우
      if distances[adjacent] > new_distance:
        # 거리 갱신
        # 우선순위 큐에 추가
        distances[adjacent] = new_distance
        heapq.heappush(heap_data, (new_distance, adjacent))

  return distances

# 시작 문자
# 노드 수, 간선 입력 받을 개수
s = 'A'
# s = 1
n, m = map(int, r().split())

graph = dict()
for _ in range(m):
  start, end, weight = r().split()
  # start, end, weight = map(int, r().split())

  # key가 있는 경우
  if start not in graph.keys():
    graph[start] = {end: int(weight)}
    # 도착 노드 key가 없는 경우
    if end not in graph.keys():
      graph[end] = {end: 0}
  # key가 없는 경우
  else:
    graph[start].update({end: int(weight)})

print('그래프: ', graph)
result = dict_dijkstra(graph, s)
print('최단거리: ', result)










# 입력 예시
# 6 9
# 1 2 8
# 1 3 1
# 1 4 2
# 3 2 5
# 3 4 2
# 4 5 3
# 4 6 5
# 5 6 1
# 6 1 5
# 6 9
# A B 8
# A C 1
# A D 2
# C B 5
# C D 2
# D E 3
# D F 5
# E F 1
# F A 5

# 출력 예시
# 그래프:  [[], [(2, 8), (3, 1), (4, 2)], [], [(2, 5), (4, 2)], [(5, 3), (6, 5)], [(6, 1)], [(1, 5)]]
# 최단거리:  [inf, 0, 6, 1, 2, 5, 6]

# 그래프:  {'A': {'B': 8, 'C': 1, 'D': 2}, 'B': {'B': 0}, 'C': {'B': 5, 'D': 2}, 'D': {'E': 3, 'F': 5}, 'E': {'E': 0, 'F': 1}, 'F': {'A': 5}}
# 최단거리:  {'A': 0, 'B': 6, 'C': 1, 'D': 2, 'E': 5, 'F': 6}