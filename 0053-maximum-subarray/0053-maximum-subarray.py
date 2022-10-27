class Solution:

	def maxSubArray(self, nums):

		currSum, resultSum = 0, float('-inf')

		for num in nums:

			resultSum = max(resultSum, currSum + num)

			currSum = max(0, currSum + num)

		return resultSum	