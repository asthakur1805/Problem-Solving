class Solution:

	def isInterleave(self,firstStr,secondStr,resultStr):

		if len(firstStr) + len(secondStr) != len(resultStr):

			return False

		dp = [[False]*(len(secondStr)+1) for _ in range(len(firstStr)+1)]
		dp[len(firstStr)][len(secondStr)] = True

		for firstIndex in range(len(firstStr),-1,-1):

			for secondIndex in range(len(secondStr),-1,-1):

				if firstIndex < len(firstStr) and firstStr[firstIndex] == resultStr[firstIndex+secondIndex] and dp[firstIndex+1][secondIndex]:

					dp[firstIndex][secondIndex] = True

				elif secondIndex < len(secondStr) and secondStr[secondIndex] == resultStr[firstIndex+secondIndex] and dp[firstIndex][secondIndex+1]:

					dp[firstIndex][secondIndex] = True

		return dp[0][0]
					
				