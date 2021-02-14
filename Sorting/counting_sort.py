
# Counting Sort(계수 정렬)

# 모든 원소의 값이 0보다 크거나 같은 조건
array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

# 모든 범위를 포함하는 리스트 생성
count = [0] * (max(array) + 1)

for i in range(len(array)):
    # 각 데이터에 해당하는 인덱스의 값 증가
    count[array[i]] += 1

# count 개수 만큼 데이터 출력
for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=' ')

# 출력 예시
# 0 0 1 1 2 2 3 4 5 5 6 7 8 9 9
