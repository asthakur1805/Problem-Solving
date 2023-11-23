class Solution:

	def sortedSquares(self,nums):

		squares = [num**2 for num in nums]

		squares.sort()

		return squares