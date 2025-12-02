class Solution:

  """
  Problem: Valid Anagram
  Difficulty: Easy
  """

  # Time: O(n) | Space: O(n)
  def isAnagram(self, s: str, t: str) -> bool:

    if len(s) != len(t): # Skips making a hashmap if the length of both strings isn't the same, returns false
      return False

    hashS = {}
    hashT = {}

    for i in range(len(s)):
      # Build the hashmaps with the letter as the key
      # and the value is how many did that letter appear in the original word
      hashS[s[i]] = 1 + hashS.get(s[i], 0)
      hashT[t[i]] = 1 + hashT.get(t[i], 0)

    for k in hashS:  # Compare the value of keys in both hashmaps
      if hashS[k] != hashT.get(k, 0):
        return False

    return True

if __name__ == '__main__':
  s = "racecar"
  t = "carrace"

  print(Solution().isAnagram(s, t))
