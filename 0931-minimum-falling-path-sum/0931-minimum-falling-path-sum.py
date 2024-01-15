class Solution:

	def minFallingPathSum(self,grid):

		order = len(grid)

		dp = [[0]*order for _ in range(order)]

		for currRow in range(order-1,-1,-1):

			for currColumn in range(order-1,-1,-1):

				if currRow == order-1:

					dp[currRow][currColumn] = grid[currRow][currColumn]

				else:

					leftDiagonal = dp[currRow+1][currColumn-1] if currColumn > 0 else float('inf')
					down = dp[currRow+1][currColumn] 
					rightDiagonal = dp[currRow+1][currColumn+1] if currColumn < order-1 else float('inf')

					dp[currRow][currColumn] = grid[currRow][currColumn] + min(leftDiagonal,down,rightDiagonal)


		result = float('inf')

		for column in range(order):

			result = min(result,dp[0][column])

		return result
		
		