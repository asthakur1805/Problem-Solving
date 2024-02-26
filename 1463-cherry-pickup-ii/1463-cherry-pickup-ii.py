class Solution:

	def cherryPickup(self,grid):

		numRows, numColumns = len(grid), len(grid[0])

		return self.helper(grid,0,0,numColumns-1,numRows,numColumns,{})

	def helper(self,grid,currRow,firstColumn,secondColumn,numRows,numColumns,cache):

		if firstColumn < 0 or firstColumn >= numColumns or secondColumn < 0 or secondColumn >= numColumns:

			return 0

		if (currRow,firstColumn,secondColumn) in cache:

			return cache[(currRow,firstColumn,secondColumn)]

		result = grid[currRow][firstColumn]

		if firstColumn != secondColumn:

			result += grid[currRow][secondColumn]

		if currRow < numRows-1:

			currMax = float('-inf')

			for firstColumnDirection in range(-1,2):

				for secondColumnDirection in range(-1,2):

					currMax = max(currMax,self.helper(grid,currRow+1,firstColumn+firstColumnDirection,secondColumn+secondColumnDirection,numRows,numColumns,cache))

			result += currMax

		cache[(currRow,firstColumn,secondColumn)] = result
		return result


					

		

				