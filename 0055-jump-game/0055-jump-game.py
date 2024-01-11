class Solution:

	def canJump(self,nums):

		dp = [False] * len(nums)

		dp[-1] = True

		for index in range(len(nums)-2,-1,-1):

			for jump in range(1,nums[index]+1):

				if index + jump < len(nums) and dp[index+jump]:

					dp[index] = True
					break

		return dp[0]