class Solution:

	def isMatch(self,firstStr,secondStr):

		dp = [[False]*(len(secondStr)+1) for _ in range(len(firstStr)+1)]

		dp[0][0] = True

		for secondIndex in range(1,len(secondStr)+1):

			for currIndex in range(1,secondIndex+1):

				if secondStr[currIndex-1] != '*':

					dp[0][secondIndex] = False
					break

			else:

				dp[0][secondIndex] = True

		for firstIndex in range(1,len(firstStr)+1):

			dp[firstIndex][0] = False

		for firstIndex in range(1,len(firstStr)+1):

			for secondIndex in range(1,len(secondStr)+1):

				if firstStr[firstIndex-1] == secondStr[secondIndex-1] or secondStr[secondIndex-1] == '?':

					dp[firstIndex][secondIndex] = dp[firstIndex-1][secondIndex-1]

				elif secondStr[secondIndex-1] == '*':

					dp[firstIndex][secondIndex] = dp[firstIndex][secondIndex-1] or dp[firstIndex-1][secondIndex]
					
				else:

					dp[firstIndex][secondIndex] = False

		return dp[len(firstStr)][len(secondStr)]