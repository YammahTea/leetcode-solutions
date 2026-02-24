class Solution:

  """
  Problem: Top K Frequent Elements
  Difficulty: Medium
  """

  # Time: O(n) | Space: O(n)
  def topKFrequent(self, nums: list[int], k: int) -> list[int]:
    countHash = {} # Hashmap will be useful to keep track of number of occurrence
    frequent = [[] for _ in range(len(nums) + 1)]
    # Make a list of lists, because we want to know the index as it will act as the frequency
    # and at that index(frequency) we will have the numbers of the same frequency
    # the list has to be bigger than the length of nums so it can act as the frequency of the number

    for num in nums:
      countHash[num] = 1 + countHash.get(num, 0)

    for n, c in countHash.items():
      frequent[c].append(n) # Based on the number of occurrence in the hashmap, we will use it as an index in the list

    result = []  # The numbers with the most frequent occurrences based on amount of K

    # COMPLEXITY NOTE: This nested loop is O(n), NOT O(n^2).
    # Although there is a loop inside a loop, the inner loop iterates over
    # buckets that collectively contain exactly N elements.
    # We visit each number exactly once across the entire process.
    for i in range(len(frequent) - 1, 0, -1):  # To start from the end of the array
      for n in frequent[i]:  # Go through the elements of the sub array and append the elements in "result" and stop when we reach K
        result.append(n)
        if len(result) == k:
          return result


    """

    This problem can be solved with a heap approach but I haven't tried it out yet

    """


if __name__ == '__main__':
  nums = [1, 2, 2, 3, 3, 3]
  k = 2

  print(Solution().topKFrequent(nums, k))

