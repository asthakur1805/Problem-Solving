class Solution:

	def minimumTotal(self,triangle):

		numRows = len(triangle)

		dp = [[0]*rowLength for rowLength in range(1,numRows+1)]

		for currRow in range(numRows-1,-1,-1):

			for currColumn in range(currRow,-1,-1):

				if currRow == numRows-1: dp[currRow][currColumn] = triangle[currRow][currColumn]

				else:

					down = dp[currRow+1][currColumn]
					diagonal = dp[currRow+1][currColumn+1]

					dp[currRow][currColumn] = triangle[currRow][currColumn] + min(down,diagonal)

		return dp[0][0]

	