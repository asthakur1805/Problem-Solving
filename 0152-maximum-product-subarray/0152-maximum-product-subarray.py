class Solution:

	def maxProduct(self,nums):

		prefix, suffix, result = 1, 1, float('-inf')

		for index in range(len(nums)):

			prefix, suffix = prefix*nums[index], suffix*nums[len(nums)-1-index]

			result = max(result,prefix,suffix)

			if prefix == 0: prefix = 1
			
			if suffix == 0: suffix = 1

		return result

			

		