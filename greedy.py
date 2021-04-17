
# Greedy Algorithm (탐욕 알고리즘)
# 설명 : 최적의 해에 가까운 값을 구할때 (매순간 최적이라고 생각되는 경우를 선택)


# 기본 탐욕 알고리즘
# 최소한의 동전 사용하기
def min_coin_count(price, coin_list):
  total_cnt = 0
  details = []
  
  # 금액이 큰 순서대로 정렬
  coin_list.sort(reverse=True)

  # 큰 금액의 동전부터 세는 반복문
  for coin in coin_list:
    # 각각의 개수
    cnt = price // coin
    # 전체 개수
    total_cnt += cnt
    # 가격 조정(계산한 값 빼기)
    price -= coin * cnt
    # 각 동전별로 저장
    details.append([coin, cnt])
  
  return total_cnt, details

coin_list = [100, 1, 50, 500]
total, details = min_coin_count(2100, coin_list)
print('총 : %d 개'%total, details)

# 출력 예시
# 총 : 5 개 [[500, 4], [100, 1], [50, 0], [1, 0]]


# 부분 배낭 문제 (Fractional Knapsack problem)
def get_max_value(item_list, capacity):
  # (가치 / 무게) 를 기준으로 큰 것부터 정렬
  item_list = sorted(item_list, key=lambda x: x[1] / x[0], reverse=True)
  total_value = 0
  item_detail = []

  # 무게 대비 가치가 큰 순서부터 넣기 시작하는 반복문
  for item in item_list:
    # 무게가 초과되지 않으면
    if capacity - item[0] >= 0:
      # 무게 조정(넣은 만큼 줄이기)
      capacity -= item[0]
      # 총 가치 계산
      total_value += item[1]
      # 넣은 물건 나열
      item_detail.append([item[0], item[1], 1])
    # 무게가 초과되면
    else:
      # 남아있는 비율 만큼만 넣기
      fraction = capacity / item[0]
      total_value += item[1] * fraction
      item_detail.append([item[0], item[1], fraction])
      break

  return total_value, item_detail

item_list = [(15, 12), (20, 10), (25, 8), (30, 5), (10, 10)] # (무게, 가치)
total_value, item_detail = get_max_value(item_list, 30)
print('총 : %d 가치'%total_value, item_detail)

# 출력 예시
# 총 : 24 가치 [[10, 10, 1], [15, 12, 1], [20, 10, 0.25]]