class Solution:

	def jump(self,nums):

		dp = [float('inf')] * len(nums)

		dp[-1] = 0

		for index in range(len(nums)-2,-1,-1):

			for jump in range(1,nums[index]+1):

				if index + jump < len(nums):

					dp[index] = min(dp[index],1+dp[index+jump])

		return dp[0]