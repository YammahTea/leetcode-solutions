class Solution:

  """
  Problem: Contains Duplicate
  Difficulty: Easy
  """

  # Solution 1: Hash map
  # Time: O(n) | Space: O(n)
  # Note: Great for finding duplicates early
  def hasDuplicate_hash(self, nums: list[int]) -> bool:

    seen = {}
    for num in nums:
      if num in seen:
        return True
      seen[num] = 1
    return False


  # Solution 2: Set
  # Time: O(n) | Space: O(n)
  # Note: Faster, but has to build the entire set before checking
  def hasDuplicate_set(self, nums: list[int]) -> bool:

    return len(set(nums)) != len(nums)


if __name__ == '__main__':
  nums = [1, 2, 3, 3]
  print(Solution().hasDuplicate_hash(nums))
  print(Solution().hasDuplicate_set(nums))
