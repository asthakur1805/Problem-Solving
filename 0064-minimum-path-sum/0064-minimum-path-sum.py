class Solution:

	def minPathSum(self,grid):

		numRows, numColumns = len(grid), len(grid[0])

		return self.helper(grid,0,0,numRows,numColumns,{})

	def helper(self,grid,currRow,currColumn,numRows,numColumns,cache):

		if currRow >= numRows or currColumn >= numColumns:

			return float('inf')

		if (currRow,currColumn) in cache:

			return cache[(currRow,currColumn)]

		result = grid[currRow][currColumn]

		if (currRow,currColumn) != (numRows-1,numColumns-1):

			down = self.helper(grid,currRow+1,currColumn,numRows,numColumns,cache)
			right = self.helper(grid,currRow,currColumn+1,numRows,numColumns,cache)

			result += min(down,right)

		cache[(currRow,currColumn)] = result
		return result