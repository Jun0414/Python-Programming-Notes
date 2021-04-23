
# Backtracking (백 트랙킹, 퇴각 검색)
# 설명 : 해를 찾기위해 후보군을 점진적으로 검색하다가, 제약조건 불만족 후보군은 앞으로 다시 보지 않을 것을 표기하며 다른 후보군으로 넘기는 기법
#       (최적의 해를 찾는 방법, DFS 방식)


# N Queen 문제

def is_available(candidate, curr_col):
  # queen의 수가 곧 행이다(매 행마다 1개의 queen만 가질 수 있으므로)
  # candidate[queen]은 순서대로 0,1,2,3 번째 행의 열index를 나타낸다 
  curr_row = len(candidate)

  for queen_row in range(curr_row):
    # queen과 같은 열이거나 대각선에 위치하면
    if candidate[queen_row] == curr_col or abs(candidate[queen_row] - curr_col) == curr_row - queen_row:
      return False
  return True

def dfs(n, curr_row, curr_candidate, final_result):
  # 마지막 행이라면
  if curr_row == n:
    final_result.append(curr_candidate[:])
    return

  # 모든 열 중에 가능한 열 찾기
  for candidate_col in range(n):
    # 가능한 열을 찾았다면
    if is_available(curr_candidate, candidate_col):
      # 후보에 저장
      curr_candidate.append(candidate_col)
      # 바로 그 다음 행을 탐색
      dfs(n, curr_row + 1, curr_candidate, final_result)
      # 다음 행에서 후보를 찾지 못하고 함수를 탈출한 경우(백 트레킹, 후보군에서 제외)
      curr_candidate.pop()

def solve_n_queens(n):
  final_result = []
  dfs(n, 0, [], final_result)

  return final_result

result = solve_n_queens(4)
print(result)