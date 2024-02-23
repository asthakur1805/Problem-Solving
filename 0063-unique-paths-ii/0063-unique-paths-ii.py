class Solution:

	def uniquePathsWithObstacles(self,obstacleGrid):

		numRows, numColumns = len(obstacleGrid), len(obstacleGrid[0])

		return self.helper(0,0,numRows,numColumns,obstacleGrid,{})

	def helper(self,currRow,currColumn,numRows,numColumns,obstacleGrid,cache):

		if currRow >= numRows or currColumn >= numColumns or obstacleGrid[currRow][currColumn] == 1:

			return 0

		if (currRow,currColumn) == (numRows-1,numColumns-1):

			return 1

		if (currRow,currColumn) in cache:

			return cache[(currRow,currColumn)]

		down = self.helper(currRow+1,currColumn,numRows,numColumns,obstacleGrid,cache)
		right = self.helper(currRow,currColumn+1,numRows,numColumns,obstacleGrid,cache)

		cache[(currRow,currColumn)] = down+right
		return cache[(currRow,currColumn)]
		