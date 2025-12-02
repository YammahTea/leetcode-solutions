from collections import defaultdict

class Solution():

  """
  Problem: Group Anagrams
  Difficulty: Medium
  """

  # Time: O(n × m log m) | Space: O(n × m)
  # n = number of strings
  # m = average length of strings, because of the sorted algorithm
  def group_anagrams(self, strs: list[str]) -> list[list[str]]:

      anagrams = defaultdict(list)

      for word in strs:
        sorted_word = tuple(sorted(word))  # So the key of the hashmap is immutable
        anagrams[sorted_word].append(word)

      return list(anagrams.values()) # Expected type is list[list[str]]


if __name__ == "__main__":
    strs = ["act", "pots", "tops", "cat", "stop", "hat"]
    sol = Solution()
    print(sol.group_anagrams(strs))
