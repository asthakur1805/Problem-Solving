class Solution:

	def runningSum(self,nums):

		result = nums.copy()

		for index in range(1,len(result)):

			result[index] += result[index-1]

		return result

		