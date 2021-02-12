
# Quick Sort(퀵 정렬)

arr = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(arr, start, end):
    # 원소가 1개인 경우 종료
    if start >= end:
        return

    # 피벗은 첫 번째 원소
    pivot = start
    left = start + 1
    right = end

    while left <= right:
        # 피벗보다 큰 원소를 찾을 때까지 반복
        while left <= end and arr[left] <= arr[pivot]:
            left += 1
        # 피벗보다 작은 원소를 찾을 때까지 반복
        while right > start and arr[right] >= arr[pivot]:
            right -= 1

        # 엇갈렸다면 작은 원소와 피벗을 교환
        if left > right:
            arr[right], arr[pivot] = arr[pivot], arr[right]
        # 엇갈리지 않았다면 작은 원소와 큰 원소를 교환
        else:
            arr[left], arr[right] = arr[right], arr[left]

    # 교환 이후 각각 왼쪽과 오른쪽 파트 정렬 수행
    quick_sort(arr, start, right - 1)
    quick_sort(arr, right + 1, end)

quick_sort(arr, 0, len(arr) - 1)

print(arr)

# 출력 예시
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]