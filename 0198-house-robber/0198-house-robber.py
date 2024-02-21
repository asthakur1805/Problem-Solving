class Solution:

	def rob(self,nums):

		secondPrev, firstPrev = 0, nums[0]

		for index in range(1,len(nums)):

			steal = nums[index] + secondPrev
			notSteal = firstPrev

			secondPrev, firstPrev = firstPrev, max(steal,notSteal)

		return firstPrev
			