class Solution:

	def subsetsWithDup(self, nums):

		nums.sort()

		index, builder, result = 0, [], []

		self.helper(nums, index, builder, result)

		return result

	def helper(self, nums, index, builder, result):

		if index == len(nums):

			result.append(builder.copy())
			return

		builder.append(nums[index])

		self.helper(nums, index+1, builder, result)

		builder.pop()

		while index < len(nums)-1 and nums[index] == nums[index+1]:

			index += 1

		self.helper(nums, index+1, builder, result)