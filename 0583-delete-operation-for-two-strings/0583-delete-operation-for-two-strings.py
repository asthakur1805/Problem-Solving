class Solution:

	def minDistance(self,firstStr,secondStr):

		return len(firstStr) + len(secondStr) - 2 * self.longestCommonSubsequence(firstStr,secondStr)

	def longestCommonSubsequence(self,firstStr,secondStr):

		prev = [0]*(len(secondStr)+1) 

		for firstIndex in range(1,len(firstStr)+1):

			dp = [0]*(len(secondStr)+1)

			for secondIndex in range(1,len(secondStr)+1):

				if firstStr[firstIndex-1] == secondStr[secondIndex-1]:

					dp[secondIndex] = 1 + prev[secondIndex-1]

				else:
					
					dp[secondIndex] = max(prev[secondIndex],dp[secondIndex-1])
		
			prev = dp

		return prev[len(secondStr)]