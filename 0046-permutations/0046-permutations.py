class Solution:

	def permute(self, nums):

		result = []

		self.helper(nums, 0, result)

		return result

	def helper(self, nums, index, result):

		if index == len(nums):
			
			result.append(nums.copy())
			return

		for swapIndex in range(index,len(nums)):

			nums[index], nums[swapIndex] = nums[swapIndex], nums[index]

			self.helper(nums, index+1, result)

			nums[index], nums[swapIndex] = nums[swapIndex], nums[index]

