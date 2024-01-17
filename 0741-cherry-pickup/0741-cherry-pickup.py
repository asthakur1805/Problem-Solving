class Solution:

	def cherryPickup(self,grid):

		order = len(grid)

		return max(0,self.helper(grid,0,0,0,order,{}))

	def helper(self,grid,firstRow,firstColumn,secondRow,order,cache):

		secondColumn = firstRow+firstColumn-secondRow

		if firstRow >= order or secondRow >= order or firstColumn >= order or secondColumn >= order or grid[firstRow][firstColumn] == -1 or grid[secondRow][secondColumn] == -1:

			return float('-inf')

		if (firstRow,firstColumn) == (order-1,order-1):

			return grid[firstRow][firstColumn]

		if (firstRow,firstColumn,secondRow) in cache:

			return cache[(firstRow,firstColumn,secondRow)]

		if (firstRow,firstColumn) == (secondRow,secondColumn):

			currCherries = grid[firstRow][firstColumn]

		else:

			currCherries = grid[firstRow][firstColumn] + grid[secondRow][secondColumn]

		bothRight = self.helper(grid,firstRow,firstColumn+1,secondRow,order,cache)
		rightDown = self.helper(grid,firstRow,firstColumn+1,secondRow+1,order,cache)
		downRight = self.helper(grid,firstRow+1,firstColumn,secondRow,order,cache)
		bothDown = self.helper(grid,firstRow+1,firstColumn,secondRow+1,order,cache)

		cache[(firstRow,firstColumn,secondRow)] = currCherries + max(bothRight,rightDown,downRight,bothDown)

		return cache[(firstRow,firstColumn,secondRow)]
		