
# key 값으로 정렬
arr = [('바나나', 2), ('사과', 5), ('당근', 3)]

def setting(data):
    # 튜플의 2번째 원소(인덱스로는 1번째)를 반환
    return data[1]

result = sorted(arr, key=setting)

print(result)

# 출력 예시
# [('바나나', 2), ('당근', 3), ('사과', 5)]