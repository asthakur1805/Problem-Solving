class Solution:

	def uniquePathsWithObstacles(self,obstacleGrid):

		return self.helper(obstacleGrid,0,0,len(obstacleGrid),len(obstacleGrid[0]),{})

	def helper(self,obstacleGrid,currRow,currColumn,numRows,numColumns,cache):

		if currRow >= numRows or currColumn >= numColumns or obstacleGrid[currRow][currColumn]:

			return 0

		if (currRow,currColumn) == (numRows-1,numColumns-1):

			return 1

		if (currRow,currColumn) in cache:

			return cache[(currRow,currColumn)]

		right = self.helper(obstacleGrid,currRow,currColumn+1,numRows,numColumns,cache)
		down = self.helper(obstacleGrid,currRow+1,currColumn,numRows,numColumns,cache)

		cache[(currRow,currColumn)] = right+down

		return cache[(currRow,currColumn)]