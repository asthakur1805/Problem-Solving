class Solution:

	def rob(self,nums):

		return max(nums[0],self.helper(nums[1:]),self.helper(nums[:-1]))

	def helper(self,nums):

		if len(nums) == 0: return 0

		firstNum, secondNum = 0, nums[0]

		for index in range(1,len(nums)):

			currRob = nums[index] + firstNum

			currSkip = secondNum

			firstNum, secondNum = secondNum, max(currRob,currSkip)

		return secondNum