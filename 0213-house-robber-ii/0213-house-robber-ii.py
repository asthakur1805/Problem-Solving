class Solution:

	def rob(self,nums):

		return max(nums[0],self.helper(nums[1:]),self.helper(nums[:-1]))

	def helper(self,nums):

		if len(nums)==0: return 0

		secondPrev, firstPrev = 0, nums[0]

		for index in range(1,len(nums)):

			rob = nums[index] + secondPrev 

			skip = firstPrev

			result = max(rob,skip)

			secondPrev = firstPrev
	
			firstPrev = result

		return firstPrev