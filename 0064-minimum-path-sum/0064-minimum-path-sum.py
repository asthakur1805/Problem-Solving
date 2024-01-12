class Solution:

	def minPathSum(self,grid):

		numRows, numColumns = len(grid), len(grid[0])

		return self.helper(grid,0,0,numRows,numColumns,{})

	def helper(self,grid,currRow,currColumn,numRows,numColumns,cache):

		if currRow >= numRows or currColumn >= numColumns:

			return float('inf')

		if (currRow,currColumn) == (numRows-1,numColumns-1):

			return grid[currRow][currColumn]

		if (currRow,currColumn) in cache:

			return cache[(currRow,currColumn)]

		right = self.helper(grid,currRow,currColumn+1,numRows,numColumns,cache)
		down = self.helper(grid,currRow+1,currColumn,numRows,numColumns,cache)

		cache[(currRow,currColumn)] = grid[currRow][currColumn] + min(right,down)

		return cache[(currRow,currColumn)]