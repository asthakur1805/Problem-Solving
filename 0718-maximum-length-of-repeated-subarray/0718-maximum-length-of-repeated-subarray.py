class Solution:

	def findLength(self,firstArr,secondArr):

		prev = [0]*(len(secondArr)+1)

		result = 0

		for firstIndex in range(1,len(firstArr)+1):

			dp = [0]*(len(secondArr)+1)

			for secondIndex in range(1,len(secondArr)+1):

				if firstArr[firstIndex-1] == secondArr[secondIndex-1]:

					dp[secondIndex] = 1 + prev[secondIndex-1]
					result = max(result,dp[secondIndex])

			prev = dp

		return result