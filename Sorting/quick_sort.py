
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



# 파이썬 전용 퀵정렬(속도는 조금 느리다)

arr = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort_py(array):
    # 리스트가 하나 이하의 원소만 담고있으면 종료
    if len(array) <= 1:
        return array

    pivot = array[0]
    # 피벗을 제외한 리스트
    tail = array[1:]

    # 분할된 왼쪽 부분
    left_side = [x for x in tail if x <= pivot]
    # 분할된 오른쪽 부분
    right_side = [y for y in tail if y > pivot]

    # 분할 이후 왼쪽과 오른쪽 부분에서 각각 정렬 수행하고, 전체 리스트 반환
    return quick_sort_py(left_side) + [pivot] + quick_sort_py(right_side)

print(quick_sort_py(arr))

# 출력 예시
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]