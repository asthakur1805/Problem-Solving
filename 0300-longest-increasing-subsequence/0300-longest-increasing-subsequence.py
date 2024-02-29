class Solution:

	def lengthOfLIS(self,nums):

		dp = [1]*len(nums)

		for currIndex in range(len(nums)-2,-1,-1):

			for prevPickedIndex in range(currIndex+1,len(nums)):

				pick = 1 + dp[prevPickedIndex] if nums[currIndex] < nums[prevPickedIndex] else 1
				notPick = dp[currIndex]

				dp[currIndex] = max(pick,notPick)

		return max(dp)



			
	
	