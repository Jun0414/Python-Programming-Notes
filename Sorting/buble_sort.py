
# Buble Sort (버블 정렬)

# 시간복잡도
# 최악 O(n^2)
# 최선 O(n)

import random

# 버블 정렬 함수 정의
def bubleSort(data):
  # 데이터 길이 -1 만큼만 실행
  for index in range(len(data) - 1):
    # 버블 정렬 최적화를 위해   
    swap = False

    # loop 돌때마다 1개씩 정렬되므로 그만큼 빼주기
    for index2 in range(len(data) - index - 1):
      # 앞의 데이터가 크다면 위치 교환
      if data[index2] > data[index2 + 1]:
        data[index2], data[index2 + 1] = data[index2 + 1], data[index2]
        swap = True
    
    # 한 loop에서 위치교환을 하지 않은 경우 (정렬 종료)
    if swap == False:
      break
  
  # 정렬된 데이터 반환
  return data


# 0 ~ 99까지 50개 랜덤하게 생성
data_list = random.sample(range(100), 50)

result = bubleSort(data_list)
print(result)