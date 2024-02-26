class Solution:

	def cherryPickup(self,grid):
	
		order = len(grid)
		
		dp = [[[float('-inf')]*order for _ in range(order)] for _ in range(order)]

		for firstRow in range(order-1,-1,-1):

			for firstColumn in range(order-1,-1,-1):

				for secondRow in range(order-1,-1,-1):

					secondColumn = firstRow+firstColumn-secondRow
		
					if 0 <= secondColumn < order and grid[firstRow][firstColumn] != -1 and grid[secondRow][secondColumn] != -1:

						dp[firstRow][firstColumn][secondRow] = grid[firstRow][firstColumn]

						if (firstRow,firstColumn) != (secondRow,secondColumn):

							dp[firstRow][firstColumn][secondRow] += grid[secondRow][secondColumn]

						if (firstRow,firstColumn) != (order-1,order-1):

							bothRight = dp[firstRow][firstColumn+1][secondRow] if firstColumn+1<order else float('-inf')
							bothDown = dp[firstRow+1][firstColumn][secondRow+1] if firstRow+1<order and secondRow+1<order else float('-inf')
							downRight = dp[firstRow+1][firstColumn][secondRow] if firstRow+1<order else float('-inf')
							rightDown = dp[firstRow][firstColumn+1][secondRow+1] if firstColumn+1<order and secondRow+1<order else float('-inf')

							dp[firstRow][firstColumn][secondRow] += max(bothRight,bothDown,downRight,rightDown)

		return max(0,dp[0][0][0])

						

			