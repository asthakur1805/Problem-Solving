class Solution:

	def rob(self,nums):

		return self.helper(nums,len(nums)-1,{})

	def helper(self,nums,index,cache):

		if index == 0: return nums[index]

		if index < 0: return 0

		if index in cache:

			return cache[index]

		rob = nums[index] + self.helper(nums,index-2,cache)

		skip = self.helper(nums,index-1,cache)

		cache[index] = max(rob,skip)

		return cache[index]
		