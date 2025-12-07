class Solution:

  """
  Problem: Valid Parentheses
  Difficulty: Easy
  """

  # Time: O(n) | Space: O(n)
  def isValid(self, s: str) -> bool:

    if len(s) % 2 != 0:
      return False # saves process if the string isn't even

    stack = []
    close_to_open = {
      ']': '[',
      '}': '{',
      ')': '('
    }

    for c in s:
      if c in close_to_open:
        if stack and stack[-1] == close_to_open[c]:
          stack.pop()
        else:
          return False
      else:
        stack.append(c)

    return True if not stack else False # this will check if the stack has leftovers (there are still open parentheses)


if __name__ == '__main__':
  s = "[](){}"
  print(Solution().isValid(s))

  s = "[](()"
  print(Solution().isValid(s))

