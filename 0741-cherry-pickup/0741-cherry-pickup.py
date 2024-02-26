class Solution:

	def cherryPickup(self,grid):

		return max(0,self.helper(grid,0,0,0,len(grid),{}))

	def helper(self,grid,firstRow,firstColumn,secondRow,order,cache):

		secondColumn = firstRow+firstColumn-secondRow

		if firstRow >= order or secondRow >= order or firstColumn >= order or secondColumn >= order or grid[firstRow][firstColumn] == -1 or grid[secondRow][secondColumn] == -1:

			return float('-inf')

		if (firstRow,firstColumn,secondColumn) in cache:

			return cache[(firstRow,firstColumn,secondColumn)]

		result = grid[firstRow][firstColumn]

		if (firstRow,firstColumn) != (secondRow,secondColumn):

			result += grid[secondRow][secondColumn]

		if (firstRow,firstColumn) != (order-1,order-1):

			bothRight = self.helper(grid,firstRow,firstColumn+1,secondRow,order,cache)
			bothDown = self.helper(grid,firstRow+1,firstColumn,secondRow+1,order,cache)
			downRight = self.helper(grid,firstRow+1,firstColumn,secondRow,order,cache)
			rightDown = self.helper(grid,firstRow,firstColumn+1,secondRow+1,order,cache)

			result += max(bothRight,bothDown,downRight,rightDown)

		cache[(firstRow,firstColumn,secondColumn)] = result
		return result

			