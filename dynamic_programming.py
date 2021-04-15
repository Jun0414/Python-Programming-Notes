
# Dynamic Programming
# 분할 정복법과 차이
# 계산한 값을 저장하고 재활용하여 효율을 높인다


# 피보나치 수열 적용

# 반복적 표현 (이 경우는 재귀보다 효율적임)
def fibo(num):
  data = [0 for index in range(num + 1)]
  data[0] = 0
  data[1] = 1

  if num <= 1:
    return data[num]

  for index in range(2, num + 1):
    data[index] = data[index - 1] + data[index - 2]
  
  return data[num]

fibo(4)


# 재귀적 표현
def fibo_dp(num):
  if num <= 1:
    return data[num]

  if data[num] == 0:
    data[num] = fibo_dp(num - 1) + fibo_dp(num - 2)
  
  return data[num]

num = 4
data = [0 for index in range(num + 1)]
data[0] = 0
data[1] = 1

print(fibo_dp(num))