class Solution:

	def runningSum(self,nums):

		if not nums:

			return []

		result = []

		result.append(nums[0])

		for index in range(1,len(nums)):

			result.append(nums[index]+result[index-1])

		return result