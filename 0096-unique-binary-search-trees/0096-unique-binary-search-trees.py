class Solution:

	def numTrees(self,upperBound):

		dp = [0]*(upperBound+1)

		dp[0] = dp[1] = 1

		for curr in range(2,upperBound+1):

			for index in range(1,curr+1):

				dp[curr] += dp[index-1]*dp[curr-index]

		return dp[upperBound]
