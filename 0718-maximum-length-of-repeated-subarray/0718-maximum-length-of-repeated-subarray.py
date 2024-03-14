class Solution:

	def findLength(self,firstArr,secondArr):

		dp = [[0]*(len(secondArr)+1) for _ in range(len(firstArr)+1)]

		result = 0

		for firstIndex in range(1,len(firstArr)+1):

			for secondIndex in range(1,len(secondArr)+1):

				if firstArr[firstIndex-1] == secondArr[secondIndex-1]:

					dp[firstIndex][secondIndex] = 1 + dp[firstIndex-1][secondIndex-1]
					result = max(result,dp[firstIndex][secondIndex])

		return result