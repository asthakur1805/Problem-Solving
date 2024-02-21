class Solution:

	def rob(self,nums):

		return max(nums[0],self.helper(nums[1:]),self.helper(nums[:-1]))

	def helper(self,nums):

		if not nums:

			return 0

		secondPrev, firstPrev = 0, nums[0]

		for index in range(1,len(nums)):

			steal = nums[index] + secondPrev
			notSteal = firstPrev

			secondPrev, firstPrev = firstPrev, max(steal,notSteal)

		return firstPrev