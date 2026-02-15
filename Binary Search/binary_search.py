class Solution:

  """
  Problem: Binary Search
  Difficulty: Easy
  """

  # Time: O(log(n)) | Space: O(1)
  def search(self, nums: list[int], target: int) -> int:

    left = 0
    right = len(nums) - 1
    mid = (right + left) // 2

    while left <= right:

      if nums[mid] == target:
        return mid

      elif nums[mid] < target:
        left = mid + 1

      else:
        right = mid - 1


      mid = (right + left) // 2

    return -1


if __name__ == '__main__':
  nums = [-1,0,2,4,6,8]
  target = 4

  print(Solution().search(nums, target)) # found at index 3
  print(Solution().search(nums, 3)) # not found (-1)

