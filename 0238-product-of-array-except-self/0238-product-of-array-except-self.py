class Solution:

	def productExceptSelf(self, nums):

		result = []

		prefix, postfix = 1, 1

		for num in nums:

			result.append(prefix)

			prefix *= num

		for index in range(len(nums)-1,-1,-1):

			result[index] *= postfix

			postfix *= nums[index]

		return result