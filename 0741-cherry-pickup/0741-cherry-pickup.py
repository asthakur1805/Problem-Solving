class Solution:

	def cherryPickup(self,grid):
	
		order = len(grid)
		
		prev = [[float('-inf')]*order for _ in range(order)] 

		for firstRow in range(order-1,-1,-1):

			dp = [[float('-inf')]*order for _ in range(order)] 

			for firstColumn in range(order-1,-1,-1):

				for secondRow in range(order-1,-1,-1):

					secondColumn = firstRow+firstColumn-secondRow
		
					if 0 <= secondColumn < order and grid[firstRow][firstColumn] != -1 and grid[secondRow][secondColumn] != -1:

						dp[firstColumn][secondRow] = grid[firstRow][firstColumn]

						if (firstRow,firstColumn) != (secondRow,secondColumn):

							dp[firstColumn][secondRow] += grid[secondRow][secondColumn]

						if (firstRow,firstColumn) != (order-1,order-1):

							bothRight = dp[firstColumn+1][secondRow] if firstColumn+1<order else float('-inf')
							bothDown = prev[firstColumn][secondRow+1] if firstRow+1<order and secondRow+1<order else float('-inf')
							downRight = prev[firstColumn][secondRow] if firstRow+1<order else float('-inf')
							rightDown = dp[firstColumn+1][secondRow+1] if firstColumn+1<order and secondRow+1<order else float('-inf')

							dp[firstColumn][secondRow] += max(bothRight,bothDown,downRight,rightDown)

			prev = dp

		return max(0,prev[0][0])

						

			
						

			