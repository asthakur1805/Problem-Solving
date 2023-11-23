class Solution:

	def sortedSquares(self,nums):

		squares, index = [0]*len(nums), len(nums)-1

		left, right = 0, len(nums)-1

		while index >= 0:

			if abs(nums[left]) >= abs(nums[right]):

				squares[index] = nums[left] ** 2
				left += 1

			else:

				squares[index] = nums[right] ** 2
				right -= 1

			index -= 1

		return squares
	
			