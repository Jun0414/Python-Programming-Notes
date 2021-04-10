
# 분할 정복 알고리즘

# Merge Sort (병합 정렬)
# 설명 : 쪼갤 수 없을때 까지 나눈 뒤, 좌우의 첫번째 아이템을 대소비교를 통해 합치며 정렬

# 시간 복잡도
# 최악 O(n log n)


import random

def merge(left, right):
  result = []

  # 두 배열 모두 비교할 아이템이 있으면 반복
  while len(left) > 0 and len(right) > 0:
    # 오른쪽이 더 작을 경우
    if left[0] > right[0]:
      result.append(right[0])
      del right[0]
    # 왼쪽이 더 작을 경우
    else:
      result.append(left[0])
      del left[0]
  
  # 왼쪽 배열에 아이템이 남아있는 경우
  if len(left) > 0:
    while len(left) > 0:
      result.append(left[0])
      del left[0]
  # 오른쪽 배열에 아이템이 남아있는 경우
  else:
    while len(right) > 0:
      result.append(right[0])
      del right[0]
  
  return result

def merge_split(arr):
  # 더이상 쪼갤 수 없는 경우
  if len(arr) <= 1:
    return arr

  # 가운데를 기점으로 좌,우 나누기
  mid = len(arr) // 2
  left = arr[:mid]
  right = arr[mid:]

  # 1개까지 쪼갠 뒤, 합치기
  return merge(merge_split(left), merge_split(right))


arr = random.sample(range(100), 20)
print(merge_split(arr))