class Solution:

	def rob(self,nums):

		firstNum, secondNum = 0, nums[0]

		for index in range(1,len(nums)):

			rob = nums[index] + firstNum

			skip = secondNum

			firstNum, secondNum = secondNum, max(rob,skip)

		return secondNum