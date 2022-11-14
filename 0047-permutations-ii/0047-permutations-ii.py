class Solution:

	def permuteUnique(self, nums):

		nums.sort()

		builder = []

		result = []

		numsUsed = [False] * len(nums)

		self.helper(nums, builder, numsUsed, result)

		return result

	def helper(self, nums, builder, numsUsed, result):

		if len(builder) == len(nums):
			
			result.append(builder.copy())
			return

		for index,num in enumerate(nums):

			if numsUsed[index] or index > 0 and nums[index] == nums[index-1] and not numsUsed[index-1]:

				continue

			numsUsed[index] = True
			builder.append(num)

			self.helper(nums, builder, numsUsed, result)

			builder.pop()
			numsUsed[index] = False
	