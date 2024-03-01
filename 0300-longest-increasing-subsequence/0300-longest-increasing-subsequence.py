class Solution:

	def lengthOfLIS(self,nums):

		dp = [1]*len(nums)

		for currIndex in range(1,len(nums)):

			for prevIndex in range(currIndex):

				pick = 1 + dp[prevIndex] if nums[prevIndex] < nums[currIndex] else float('-inf')
				notPick = dp[currIndex]

				dp[currIndex] = max(pick,notPick)
		
		return max(dp)