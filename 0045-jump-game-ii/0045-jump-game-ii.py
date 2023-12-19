class Solution:

	def jump(self,nums):

		dp = [0]*len(nums)

		for index in range(len(nums)-2,-1,-1):
		
			dp[index] = float('inf')

			for jump in range(1,nums[index]+1):

				if index + jump < len(nums):

					dp[index] = min(dp[index],1+dp[index+jump])

		return dp[0]

		
		