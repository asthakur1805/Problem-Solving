class Solution:

	def permuteUnique(self, nums):

		nums.sort()

		result = []

		self.helper(nums, 0, result)

		return result

	def helper(self, nums, index, result):

		if index == len(nums):

			result.append(nums.copy())
			return

		for swapIndex in range(index,len(nums)):

			if swapIndex == index or nums[swapIndex] != nums[index]:


			    nums[index], nums[swapIndex] = nums[swapIndex], nums[index]

			    self.helper(nums.copy(), index+1, result)   