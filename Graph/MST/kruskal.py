
# Minimum Spanning Tree (MST 최소 신장 트리)
# 신장 트리 : 모든 노드가 연결 O, 동시에 사이클 X 인 트리


# Kruskal's algorithm (크루스칼 알고리즘)(대표적 최소신장트리1)
# 설명 : 모든 정점을 비용이 적은 것부터 연결하여 cycle이 형성되지 않는 트리 구조 (탐욕 알고리즘 기초)

  # Union-Find algorithm
  # 설명 : 노드들 중 연결된 노드를 찾거나 서로 연결할 때 사용 (Disjoint Set(서로소 집합)을 표현할 때 사용)
  #        cycle 없는 것을 찾을 때 유용

  # 두 트리 집합의 높이가 다르다면, 높은 쪽에 낮은 트리를 연결
  # 두 트리 집합의 높이가 같다면, 아무쪽이나 랭크를 증가시켜 그 밑으로 다른하나를 붙인다

# 시간복잡도 (V : 정점 수, E : 간선 수)
# kruskal 시간복잡도 O(V)
# 정렬 시간복잡도 O(E log E)
# find,union 시간복잡도 O(E)
# **최악 O(E log E)

import sys
r = sys.stdin.readline


def find(v):
  # 현재 v가 root가 아닌 경우
  if parent[v] != v:
  # 현재 v가 root일때 까지 재귀로 찾아서 반환
    parent[v] = find(parent[v])
  
  return parent[v]


def union(v1, v2):
  root1 = find(v1)
  root2 = find(v2)

  # 같은 트리인 경우
  if root1 == root2:
    return
  # root1의 깊이가 더 깊은 경우
  if rank[root1] > rank[root2]:
    parent[root2] = root1
  # root2의 깊이가 더 깊거나 동일한 경우
  else:
    parent[root1] = root2
    # 깊이가 동일하면(root1의 부모를 root2로 설정 했으므로)
    if rank[root1] == rank[root2]:
      rank[root2] += 1


# 크루스칼 알고리즘
def kruskal(edges):
  # 비용이 낮은 순으로 정렬
  edges.sort(key=lambda x: x[2])
  total = 0
  mst = []

  for v1, v2, cost in edges:
    # 서로 다른 집합인 경우
    if find(v1) != find(v2):
      union(v1, v2)
      total += cost
      mst.append((v1, v2))
        
  return total, mst


# 정점 수, 간선 수
n, m = map(int, r().split())
# 깊이와 부모노드 초기화
rank = {v: 0 for v in range(1, n + 1)}
parent = {v: v for v in range(1, n + 1)}

edges = []
for _ in range(m):
  # 간선 추가
  start, end, cost = map(int, r().split())
  edges.append((start, end, cost))

total, mst = kruskal(edges)
print('total: ', total)
print('MST: ', mst)






# 입력 예시
# 7 22
# 1 2 7
# 1 4 5
# 2 1 7
# 2 3 8
# 2 4 9
# 2 5 7
# 3 2 8
# 3 5 5
# 4 1 5
# 4 2 7
# 4 5 7
# 4 6 6
# 5 2 7
# 5 3 5
# 5 4 7
# 5 6 8
# 5 7 9
# 6 4 6
# 6 5 8
# 6 7 11
# 7 5 9
# 7 6 11

# 출력 예시
# total:  39
# MST:  [(1, 4), (3, 5), (4, 6), (1, 2), (2, 5), (5, 7)]