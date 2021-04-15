
# Sequential Search (순차탐색)
# 설명 : 앞에서부터 차례대로 검색하며 찾는다

# 시간복잡도
# 최악 O(n)


def sequential_search(n, target, array):
    # 원소를 하나씩 확인
    for i in range(n):
        # 찾고자하는 원소인 경우(인덱스가 0부터이므로 +1해서 반환)
        if array[i] == target:
            return i + 1

print('생성할 원소 개수를 입력 후, 한 칸 띄고 찾고자하는 이름을 입력하시오.')

input_data = input().split()

# 원소 개수
n = int(input_data[0])
# 찾고자하는 문자열
target = input_data[1]

print('원소 개수만큼 이름을 한칸 띄어쓰기 단위로 적으시오.')
name_data = list(map(str, input().split()))

# 결과 출력
print(sequential_search(n, target, name_data))

# 입력 예시
# 5 철수
# 영희 영철 철수 짱구 백구

# 출력 예시
# 3
