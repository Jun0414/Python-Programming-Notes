
# Insertion Sort(삽입 정렬)
# 설명 : 현재 index를 기준으로 앞에 위치한 원소를 하나씩 비교하며 자신의 원소보다 큰 경우 즉시 위치교환하고
#        작은 원소가 나올 때 까지 반복 또는 더 이상 비교할 원소가 없을 때 까지 반복

# 시간복잡도
# 최악 O(n^2)
# 최선 O(n)

# 삽입 정렬 함수 정의
def insertionSort(data):
    # 2번째 원소부터 끝까지
    for i in range(1, len(data)):
        # 인덱스 i부터 1까지 감소하며 반복
        for j in range(i, 0, -1):
            # 앞의 원소보다 작으면 한칸씩 이동
            if data[j] < data[j - 1]:
                data[j], data[j - 1] = data[j - 1], data[j]
            # 앞의 원소보다 크면 위치 멈춤
            else:
                break
    
    return data

# 정렬할 리스트
data = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

result = insertionSort(data)
print(result)

# 출력 예시
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]