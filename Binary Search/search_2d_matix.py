class Solution:

  """
  Problem: Search a 2D Matrix
  Difficulty: Medium
  """

  # Solution 1 (optimal)
  # Time: O(log(m * n)) | Space: O(1)
  # do binary search on the matrix rows and check if the target is in the range of the current row
  # if it is, you skip and move to the second binary search to check if it exists in the possible row
  def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:

    left = 0
    right = len(matrix) - 1
    row = (right + left) // 2
    possible_list = matrix[row]
    while left <= right:
      first_element = possible_list[0] # first element (first column) in the current row
      last_element = possible_list[-1] # last element (last column) in the current row

      if first_element <= target <= last_element:
        break
        # it means, the target is in the range of the current row
        # and we found the row to check

      elif first_element > target:
        right = row - 1

      elif last_element < target:
        left = row + 1

      row = (right + left) // 2
      possible_list = matrix[row]

    if left > right:
      return False
      # means the number was not found in any range so no need to do the second binary search

    low = 0
    high = len(possible_list) - 1
    mid = (high + low) // 2

    while low <= high:
      if possible_list[mid] == target:
        return True

      elif possible_list[mid] < target:
        low = mid + 1

      else:
        high = mid - 1

      mid = (high + low) // 2

    return False


  # Solution 2 (not the best)
  # because of one useful info in the question
  # ("The first integer of every row is greater than the last integer of the previous row")
  # Time: O(m * log(n)) | Space: O(1)
  def searchMatrixSlow(self, matrix: list[list[int]], target: int) -> bool:

    for i in range(len(matrix)):
      n = matrix[i] # inner list

      # pointers inside the inner list
      left = 0
      right = len(n) - 1
      mid = (right + left) // 2
      while left <= right:

        if n[mid] == target:
          return True

        elif n[mid] < target:
          left = mid + 1

        else:
          right = mid - 1

        mid = (right + left) // 2

    return False


if __name__ == '__main__':
  matrix = [[1, 2, 4, 8], [10, 11, 12, 13], [14, 20, 30, 40]]
  target = 10

  print(Solution().searchMatrix(matrix, target))