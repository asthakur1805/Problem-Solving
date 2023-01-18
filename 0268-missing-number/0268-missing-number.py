class Solution:

	def missingNumber(self, nums):

		result = 0

		for index in range(len(nums)):

			result = result ^ index ^ nums[index]

		return result ^ len(nums)