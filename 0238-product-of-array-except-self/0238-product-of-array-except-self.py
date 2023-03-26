class Solution:

	def productExceptSelf(self, nums):

		result = [1]*len(nums)

		prefix, postfix = 1, 1

		for index in range(len(nums)):

			result[index] *= prefix
			prefix *= nums[index]

		for index in range(len(nums)-1,-1,-1):

			result[index] *= postfix
			postfix *= nums[index]

		return result