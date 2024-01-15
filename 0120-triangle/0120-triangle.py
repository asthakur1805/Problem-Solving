class Solution:

	def minimumTotal(self,triangle):

		numRows = len(triangle)

		prev = triangle[-1].copy()

		for currRow in range(numRows-2,-1,-1):

			dp = [0]*(currRow+1)

			for currColumn in range(currRow,-1,-1):

				down = prev[currColumn]
				diagonal = prev[currColumn+1]

				dp[currColumn] = triangle[currRow][currColumn] + min(down,diagonal)

			prev = dp

		return prev[0]
	