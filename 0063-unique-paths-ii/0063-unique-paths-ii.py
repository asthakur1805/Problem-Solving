class Solution:

	def uniquePathsWithObstacles(self,obstacleGrid):

		numRows, numColumns = len(obstacleGrid), len(obstacleGrid[0])

		dp = [[0]*numColumns for _ in range(numRows)]

		for currRow in range(numRows-1,-1,-1):

			for currColumn in range(numColumns-1,-1,-1):

				if obstacleGrid[currRow][currColumn]:

					dp[currRow][currColumn] = 0

				elif (currRow,currColumn) == (numRows-1,numColumns-1):

					dp[currRow][currColumn] = 1
				
				else:
					
					right = dp[currRow][currColumn+1] if currColumn < numColumns-1 else 0
					down = dp[currRow+1][currColumn] if currRow < numRows-1 else 0

					dp[currRow][currColumn] = right+down

		return dp[0][0]