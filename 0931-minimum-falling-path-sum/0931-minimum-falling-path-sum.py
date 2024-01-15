class Solution:

	def minFallingPathSum(self,grid):

		order = len(grid)

		prev = grid[-1].copy()

		for currRow in range(order-2,-1,-1):

			dp = [0]*order

			for currColumn in range(order-1,-1,-1):

				leftDiagonal = prev[currColumn-1] if currColumn > 0 else float('inf')
				down = prev[currColumn]
				rightDiagonal = prev[currColumn+1] if currColumn < order-1 else float('inf')

				dp[currColumn] = grid[currRow][currColumn] + min(leftDiagonal,down,rightDiagonal)

			prev = dp

		result = float('inf')

		for column in range(order):

			result = min(result,prev[column])

		return result

			