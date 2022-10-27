class Solution:

	def maxSubArray(self, nums):

		currSum, resultSum = 0, float('-inf')

		for num in nums:

			currSum += num

			resultSum = currSum if currSum > resultSum else resultSum

			currSum = 0 if currSum < 0 else currSum
			
		return resultSum	