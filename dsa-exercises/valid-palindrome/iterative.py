def is_valid_palindrome(phrase: str) -> bool:
  left = 0
  right = len(phrase) - 1

  while left < right:
    if not phrase[left].isalnum():
      left += 1
      continue
    if not phrase[right].isalnum():
      right -= 1
      continue
    if phrase[left].lower() == phrase[right].lower():
      left += 1
      right -= 1
    else:
      return False

  return True
      
print(is_valid_palindrome("ab b a"))
print(is_valid_palindrome("A man, a plan, a canal: Panama"))
print(is_valid_palindrome("rAce a Car"))
print(is_valid_palindrome("A"))
print(is_valid_palindrome(" "))