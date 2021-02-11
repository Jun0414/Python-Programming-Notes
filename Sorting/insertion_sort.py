
# Insertion Sort(삽입 정렬)

arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(arr)):
    # 인덱스 i부터 1까지 감소하며 반복
    for j in range(1, 0, -1):
        # 앞의 원소보다 작으면 한칸씩 이동
        if arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
        # 앞의 원소보다 크면 위치 멈춤
        else:
            break

print(arr)

# 출력 예시
# [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]