class Solution:

	def longestCommonSubsequence(self,firstStr,secondStr):

		dp = [[0]*(len(secondStr)+1) for _ in range(len(firstStr)+1)]

		for firstIndex in range(1,len(firstStr)+1):

			for secondIndex in range(1,len(secondStr)+1):

				if firstStr[firstIndex-1] == secondStr[secondIndex-1]:

					dp[firstIndex][secondIndex] = 1 + dp[firstIndex-1][secondIndex-1]

				else:
					
					dp[firstIndex][secondIndex] = max(dp[firstIndex-1][secondIndex],dp[firstIndex][secondIndex-1])
		
		return dp[len(firstStr)][len(secondStr)]

		
		


		
		
