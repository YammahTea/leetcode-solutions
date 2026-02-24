class Solution:
  """
  Problem: Product of Array Except Self
  Difficulty: Medium
  """

  # Time: O(N) | Space: O(N)
  def productExceptSelf(self, nums: list[int]) -> list[int]:
    n = len(nums)
    left_product = [0] * n
    right_product = [0] * n

    # no elements on the left
    left_product[0] = 1

    # make left product
    for i in range(1, n):
      left_product[i] = left_product[i - 1] * nums[i-1]


    """ another way to do left product """
    # for i in range(0, n):  # start from the start
    #   if i - 1 < 0: # no elements on the left
    #     left_product[0] = 1   # first element
    #   else:
    #     left_product[i] = left_product[i - 1] * nums[i-1]



    # no elements on the right
    right_product[n - 1] = 1  # last element

    # make right product
    # start at n-2 (second to last item).
    # Go down to -1 (so it stops at 0).
    for i in range(n - 2, -1, -1):
      right_product[i] = right_product[i + 1] * nums[i+1]


    """ another way to do right product """
    # for i in reversed(range(0, n)):  # start from the end
    #   if i == n - 1: # no elements on the right
    #     right_product[n - 1] = 1  # last element
    #   else:
    #     right_product[i] = right_product[i + 1] * nums[i+1]

    answer = [0] * n
    for i in range(n):
      answer[i] = left_product[i] * right_product[i]

    return answer



  """ A FOLLOW UP INTERVIEW QUESTION FOR A SOLUTION WITH O(1) SPACE (excluding the output array) """
  # Time: O(N) | Space: O(1) (output array doesn't count)
  def betterProduct(self, nums: list[int]) -> list[int]:
    n = len(nums)
    answer = [0] * n

    # 1- Calculate "Left" products directly into answer
    answer[0] = 1
    for i in range(1, n):
      answer[i] = answer[i - 1] * nums[i - 1]

    # 2- Calculate "Right" products on the fly and multiply, think of it as a snowball
    right_product = 1
    for i in reversed(range(n)):
      answer[i] = answer[i] * right_product
      right_product *= nums[i]  # Update snowball for next iteration

    return answer


if __name__ == '__main__':
  nums = [1, 2, 3, 4]

  answer = Solution().productExceptSelf(nums)
  print(answer)

  # this is a better solution using O(1) space complexity (output array doesn't count)
  answer = Solution().betterProduct(nums)
  print(answer)
