
# Selection Sort(선택 정렬)

# 정렬할 리스트
arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# 리스트 길이만큼 반복
for i in range(len(arr)):
    # 시작 인덱스를 가장 작은 값으로 설정
    min_index = i

    # 그 다음 인덱스부터 검색
    for j in range(i + 1, len(arr)):
        # 더 작은 값을 발견 시, min_index 갱신
        if arr[min_index] < arr[j]:
            min_index = j

    # 스와이프(다르면 교체효과, 같다면 그대로 인것처럼 보인다)
    arr[i], arr[min_index] = arr[min_index], arr[i]

print(arr)

# 출력 예시
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]