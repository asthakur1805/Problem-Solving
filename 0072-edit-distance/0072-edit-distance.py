class Solution:

	def minDistance(self,firstStr,secondStr):

		dp = [[0]*(len(secondStr)+1) for _ in range(len(firstStr)+1)]

		for firstIndex in range(len(firstStr)+1):

			dp[firstIndex][0] = firstIndex
		
		for secondIndex in range(len(secondStr)+1):

			dp[0][secondIndex] = secondIndex

		for firstIndex in range(1,len(firstStr)+1):

			for secondIndex in range(1,len(secondStr)+1):

				if firstStr[firstIndex-1] == secondStr[secondIndex-1]: 

					dp[firstIndex][secondIndex] = dp[firstIndex-1][secondIndex-1]

				else:

					insertion = dp[firstIndex][secondIndex-1]
					deletion = dp[firstIndex-1][secondIndex]
					replacement = dp[firstIndex-1][secondIndex-1]

					dp[firstIndex][secondIndex] = 1 + min(insertion,deletion,replacement)

		return dp[len(firstStr)][len(secondStr)]