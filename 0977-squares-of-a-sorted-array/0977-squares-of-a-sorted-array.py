class Solution:

	def sortedSquares(self,nums):

		left, right = 0, len(nums)-1

		squares = [0] * len(nums)

		for index in range(len(squares)-1,-1,-1):

			if abs(nums[left]) >= abs(nums[right]):

				squares[index] = nums[left]**2

				left += 1

			else:

				squares[index] = nums[right]**2

				right -= 1

		return squares


				