# 회문 판독 함수

def palindrome(string):
  if len(string) <= 1:
    return True
  
  if string[0] == string[-1]:
    return palindrome(string[1:-1])

  return False

word = 'level'
print(palindrome(word))