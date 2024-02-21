class Solution:

	def rob(self,nums):

		dp = [0] * len(nums)

		dp[0] = nums[0]

		for index in range(1,len(nums)):

			steal = nums[index] + (dp[index-2] if index > 1 else 0)
			dontSteal = dp[index-1]

			dp[index] = max(steal,dontSteal)

		return dp[len(nums)-1]
			