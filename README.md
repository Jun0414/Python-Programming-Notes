# 📒 Algorithm Note
---

### 📋 구성도
```
┏━ else
┃   ┣━ backtracking.py
┃   ┣━ dynamic_programming.py
┃   ┣━ greedy.py
┃   ┗━ palindrome.py
┃
┣━ Graph
┃   ┣━ MST
┃   ┃   ┣━ kruskal.py(예정)
┃   ┃   ┗━ prim.py (예정)
┃   ┣━ bfs.py
┃   ┣━ dfs.py
┃   ┗━ dijkstra.py(예정)
┃
┣━ Searhing
┃   ┣━ binary_search.py
┃   ┗━ sequential_search.py
┃
┣━ Sorting
┃   ┣━ buble_sort.py
┃   ┣━ counting_sort.py
┃   ┣━ insertion_sort.py
┃   ┣━ key_value_sort.py
┃   ┣━ merge_sort.py
┃   ┣━ quick_sort.py
┃   ┗━ selection_sort.py
┃
┗━ 
```

### 🔎 메커니즘 (Mechanism)
---
⭐️ `다익스트라 (Dijkstra Algorithm)`
- 첫 정점을 기준으로 연결되어 있는 정점들을 추가하며, 최단 거리를 갱신하는 방법 (BFS와 유사)

참고 : [다익스트라 설명](https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/?ref=leftbar-rightbar)

⭐️ `크루스칼 (Kruskal Algorithm)`
- 모든 정점을 비용이 적은 것부터 연결하며, cycle이 형성되지 않는 트리 구조 방법 (탐욕 알고리즘 기초)

참고 : [다익스트라 설명](https://www.geeksforgeeks.org/kruskals-minimum-spanning-tree-algorithm-greedy-algo-2/?ref=lbp)
