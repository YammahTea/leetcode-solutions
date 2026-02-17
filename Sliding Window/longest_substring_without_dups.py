class Solution:

  """
  Problem: Longest Substring Without Repeating Characters
  Difficulty: Medium
  """

  # Time: O(n) | Space: O(n)
  def lengthOfLongestSubstring(self, s: str) -> int:

    left = 0
    longest = 0
    sett = set()

    for right in range(len(s)):
      while s[right] in sett:
        sett.remove(s[left])
        left += 1
        # this does NOT make it a O(n²) because the left pointer is still moving
        # meaning that we are still traversing the array/string
        # so the total number of times 'left' moves across the whole program is at most 'n'
        # NOT 'n' per iteration

      window = (right - left) + 1
      longest = max(longest, window)
      sett.add(s[right])

    return longest

if __name__ == '__main__':

  s = "zxyzxyz"
  print(Solution().lengthOfLongestSubstring(s))