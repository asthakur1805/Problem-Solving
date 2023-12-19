class Solution:

	def minPathSum(self,grid):

		numRows, numColumns = len(grid), len(grid[0])

		dp = [[0]*numColumns for _ in range(numRows)]

		for currRow in range(numRows-1,-1,-1):

			for currColumn in range(numColumns-1,-1,-1):

				if (currRow,currColumn) == (numRows-1,numColumns-1):

					dp[currRow][currColumn] = grid[currRow][currColumn]

				else:
					
					right = dp[currRow][currColumn+1] if currColumn < numColumns-1 else float('inf')
					down = dp[currRow+1][currColumn] if currRow < numRows-1 else float('inf')

					dp[currRow][currColumn] = grid[currRow][currColumn] + min(right,down)

		return dp[0][0]

					
