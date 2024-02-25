class Solution:

	def minimumTotal(self,triangle):

		dp = [[0]*currColumn for currColumn in range(1,len(triangle)+1)]

		for currRow in range(len(triangle)-1,-1,-1):

			for currColumn in range(currRow,-1,-1):

				dp[currRow][currColumn] = triangle[currRow][currColumn]

				if currRow < len(triangle)-1:

					down = dp[currRow+1][currColumn]
					downRight = dp[currRow+1][currColumn+1]

					dp[currRow][currColumn] += min(down,downRight)

		return dp[0][0]