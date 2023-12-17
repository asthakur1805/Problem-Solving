class Solution:

	def rob(self,nums):

		secondPrev, firstPrev = 0, nums[0]

		for index in range(1,len(nums)):

			rob = nums[index] + secondPrev 

			skip = firstPrev

			result = max(rob,skip)

			secondPrev = firstPrev
	
			firstPrev = result

		return firstPrev