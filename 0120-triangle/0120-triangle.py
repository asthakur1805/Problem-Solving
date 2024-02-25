class Solution:

	def minimumTotal(self,triangle):

		prev = [0]*len(triangle)

		for currRow in range(len(triangle)-1,-1,-1):

			dp = [0]*(currRow+1) 

			for currColumn in range(currRow,-1,-1):

				dp[currColumn] = triangle[currRow][currColumn]

				if currRow < len(triangle)-1:

					down = prev[currColumn]
					downRight = prev[currColumn+1]

					dp[currColumn] += min(down,downRight)

			prev = dp

		return prev[0]