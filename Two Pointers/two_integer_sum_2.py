class Solution:

  """
  Problem: Two Integer Sum II
  Difficulty: Medium
  """

  # Time: O(n) | Space: O(1)
  def twoSum(self, numbers: list[int], target: int) -> list[int]:

    left = 0
    right = len(numbers) - 1

    # you can't use a map like in "Two Sum" problem, this is a constraint from the question
    # and sense the numbers are in ascending order, you can check their total
    # if it is higher than the target, you move the right pointer until you get a lower total
    # if the total is lower than the target, then it's left pointer turn to move
    # and the question guarantees that there is ALWAYS a solution
    while numbers[left] + numbers[right] != target:

      if numbers[left] + numbers[right] > target:
        right -= 1

      else:
        left += 1

    return [left + 1, right + 1]  # cuz it is 1-based