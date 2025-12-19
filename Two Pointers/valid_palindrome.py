class Solution:

  """
  Problem: Valid Palindrome
  Difficulty: Easy
  """

  # Time: O(n) | Space: O(1)
  def isPalindrome(self, s: str) -> bool:
    left = 0
    right = len(s) - 1

    while left < right:
      if not s[left].isalnum():
        left += 1
        continue

      if not s[right].isalnum():
        right -= 1
        continue

      if s[left].lower() == s[right].lower():
        # Update the index until the end of the loop
        left += 1
        right -= 1

      else:  # The character at the right isn't the same as the left, we exist the loop
        return False
    return True

if __name__ == '__main__':
  s = "Was it a car or a cat I saw?"
  print(Solution().isPalindrome(s))

  s = "tab a cat"
  print(Solution().isPalindrome(s))

