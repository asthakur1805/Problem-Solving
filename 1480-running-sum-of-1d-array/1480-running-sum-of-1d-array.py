class Solution:

	def runningSum(self,nums):

		currSum, result = 0, []

		for num in nums:

			currSum += num

			result.append(currSum)

		return result