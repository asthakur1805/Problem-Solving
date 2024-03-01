class Solution:

	def lengthOfLIS(self,nums):

		next = [0]*(len(nums)+1)

		for currIndex in range(len(nums)-1,-1,-1):

			dp = [0]*(len(nums)+1)

			for prevIndex in range(currIndex-1,-2,-1):

					pick = 1 + next[currIndex+1] if prevIndex == -1 or nums[currIndex] > nums[prevIndex] else float('-inf')
					notPick = next[prevIndex+1]			

					dp[prevIndex+1] = max(pick,notPick)

			next = dp

		return next[0]

		
		