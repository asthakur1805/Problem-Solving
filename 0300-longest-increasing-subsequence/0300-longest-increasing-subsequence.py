class Solution:

	def lengthOfLIS(self,nums):

		dp = [[0]*(len(nums)+1) for _ in range(len(nums)+1)]

		for currIndex in range(len(nums)-1,-1,-1):

			for prevIndex in range(currIndex-1,-2,-1):

					pick = 1 + dp[currIndex+1][currIndex+1] if prevIndex == -1 or nums[currIndex] > nums[prevIndex] else float('-inf')
					notPick = dp[currIndex+1][prevIndex+1]			

					dp[currIndex][prevIndex+1] = max(pick,notPick)

		return dp[0][0]

		