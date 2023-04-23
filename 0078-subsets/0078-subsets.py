class Solution:

	def subsets(self, nums):

		builder, result = [], []

		self.helper(nums, 0, builder, result)

		return result

	def helper(self, nums, index, builder, result):

		if index == len(nums):

			result.append(builder.copy())

			return 

		builder.append(nums[index])

		self.helper(nums, index+1, builder, result)

		builder.pop()

		self.helper(nums, index+1, builder, result)