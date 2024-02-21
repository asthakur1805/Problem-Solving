class Solution:

	def jump(self,nums):

		dp = [0]*len(nums)

		for index in range(len(nums)-2,-1,-1):

			dp[index] = float('inf')

			for jumpSize in range(1,nums[index]+1):

				if index + jumpSize < len(nums):

					dp[index]=min(dp[index],1+dp[index+jumpSize])

		return dp[0]

			

					