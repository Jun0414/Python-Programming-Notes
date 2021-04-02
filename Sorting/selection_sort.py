
# Selection Sort(선택 정렬)
# 설명 : 현재 원소보다 작고, index가 뒤에 있는 원소들 중 가장 작은 원소를 찾아 위치 교환

# 시간복잡도
# 최악 O(n^2)

# 선택 정렬 함수 정의
def selectionSort(data):
    # 리스트 길이보다 1 적은 만큼 반복
    for i in range(len(data) - 1):
        # 시작 인덱스를 가장 작은 값으로 설정
        min_index = i

        # 그 다음 인덱스부터 검색
        for j in range(i + 1, len(data)):
            # 더 작은 값을 발견 시, min_index 갱신
            if data[min_index] > data[j]:
                min_index = j

        # 스와이프(다르면 교체효과, 같다면 그대로 인것처럼 보인다)
        data[i], data[min_index] = data[min_index], data[i]
    
    return data

# 정렬할 리스트
data = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

result = selectionSort(data)
print(result)

# 출력 예시
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]