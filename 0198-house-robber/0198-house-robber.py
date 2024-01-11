class Solution:

	def rob(self,nums):

		dp = [0]*len(nums)

		dp[0] = nums[0]

		for index in range(1,len(nums)):

			rob = nums[index] + (dp[index-2] if index > 1 else 0)

			skip = dp[index-1]

			dp[index] = max(rob,skip)

		return dp[len(nums)-1]