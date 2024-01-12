class Solution:

	def uniquePathsWithObstacles(self,obstacleGrid):

		numRows, numColumns = len(obstacleGrid), len(obstacleGrid[0])

		prev = [0] * numColumns

		for currRow in range(numRows-1,-1,-1):

			dp = [0] * numColumns

			for currColumn in range(numColumns-1,-1,-1):

				if obstacleGrid[currRow][currColumn]:

					dp[currColumn] = 0

				elif (currRow,currColumn) == (numRows-1,numColumns-1):

					dp[currColumn] = 1

				else:

					right = dp[currColumn+1] if currColumn+1<numColumns else 0
					down = prev[currColumn]

					dp[currColumn] = right+down

			prev = dp

		return dp[0]