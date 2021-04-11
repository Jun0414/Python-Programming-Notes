
# 분할 정복 알고리즘

# Binary Search (이진탐색)
# 설명 : 배열이 정렬되어있다(필수), 가운데 값을 기준으로 크면 오른쪽을 탐색, 작으면 왼쪽을 탐색

# 시간복잡도
# 최악 O(log n)

# 재귀적 이진탐색 구현

def recursive_binary_search(arr, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2

    # 찾은 경우 중간점 인덱스 반환
    if arr[mid] == target:
        return mid
    # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif arr[mid] > target:
        return recursive_binary_search(arr, target, start, mid - 1)
    # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    else:
        return recursive_binary_search(arr, target, mid + 1, end)

# 원소 개수와 찾고자하는 문자열 입력
n, target = map(int, input().split())
# 전체 원소 입력
arr = list(map(int, input().split()))

# 이진탐색 결과 출력
result = recursive_binary_search(arr, target, 0, n - 1)

# 원소가 없다면
if result == None:
    print("원소가 존재하지 않습니다.")
# 원소가 있다면 인덱스 + 1(0번째부터 시작이므로)
else:
    print(result + 1)

# 입력 예시
# 1)
# 10 7
# 1 3 5 7 9 11 13 15 17 19
# 2)
# 10 7
# 1 3 5 6 9 11 13 15 17 19

# 출력 예시
# 1)
# 4
# 2)
# 원소가 존재하지 않습니다.