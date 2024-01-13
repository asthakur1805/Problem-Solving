class Solution:

	def minPathSum(self,grid):

		numRows, numColumns = len(grid), len(grid[0])

		prev = [float('inf')] * numColumns

		for currRow in range(numRows-1,-1,-1):

			dp = [0] * numColumns

			for currColumn in range(numColumns-1,-1,-1):

				if (currRow,currColumn) == (numRows-1,numColumns-1):

					dp[currColumn] = grid[currRow][currColumn]

				else:

					right = dp[currColumn+1] if currColumn+1<numColumns else float('inf')
					down = prev[currColumn]

					dp[currColumn] = grid[currRow][currColumn] + min(right,down)

			prev = dp

		return dp[0]