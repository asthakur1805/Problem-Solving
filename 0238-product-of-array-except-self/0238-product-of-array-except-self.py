class Solution:

	def productExceptSelf(self, nums):

		result = [1] * len(nums)

		prefixProduct, postfixProduct = 1, 1

		for index in range(len(nums)):

			result[index] = prefixProduct
			prefixProduct *= nums[index]

		for index in range(len(nums)-1,-1,-1):

			result[index] *= postfixProduct
			postfixProduct *= nums[index]

		return result
		