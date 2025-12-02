class Solution:

  """
  Problem: Two Sum
  Difficulty: Easy
  """

  # Time: O(n) | Space: 0(n)
  def twoSum(self, nums: list[int], target: int) -> list[int]:
    numbers_map = {}

    for i, num in enumerate(nums):

      if target - num in numbers_map.keys():

        return [numbers_map[target - num], i]
      numbers_map[num] = i

    return None

if __name__ == '__main__':
  nums = [3, 4, 5, 6]
  target = 7
  print(Solution().twoSum(nums, target))
