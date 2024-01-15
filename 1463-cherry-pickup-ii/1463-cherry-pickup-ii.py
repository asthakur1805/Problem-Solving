class Solution:

	def cherryPickup(self,grid):

		numRows,numColumns = len(grid),len(grid[0])

		return self.helper(grid,0,0,numColumns-1,numRows,numColumns,{})

	def helper(self,grid,row,firstColumn,secondColumn,numRows,numColumns,cache):

		if firstColumn < 0 or firstColumn >= numColumns or secondColumn < 0 or secondColumn >= numColumns:

			return 0

		if row == numRows-1:

			if firstColumn == secondColumn:

				return grid[row][firstColumn]

			return grid[row][firstColumn] + grid[row][secondColumn]

		if (row,firstColumn,secondColumn) in cache:

			return cache[(row,firstColumn,secondColumn)]

		if firstColumn == secondColumn:

			currCherries = grid[row][firstColumn]

		else:

			currCherries = (grid[row][firstColumn] + grid[row][secondColumn])

		maxResult = float('-inf')

		for firstColumnDirection in range(-1,2):

			for secondColumnDirection in range(-1,2):

				maxResult = max(maxResult,self.helper(grid,row+1,firstColumn+firstColumnDirection,secondColumn+secondColumnDirection,numRows,numColumns,cache))

		cache[(row,firstColumn,secondColumn)] = currCherries + maxResult

		return cache[(row,firstColumn,secondColumn)]