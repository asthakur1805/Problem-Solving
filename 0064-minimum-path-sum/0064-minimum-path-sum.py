class Solution:

	def minPathSum(self,grid):

		numRows, numColumns = len(grid), len(grid[0])

		dp = [[0]*numColumns for _ in range(numRows)]

		for currRow in range(numRows-1,-1,-1):

			for currColumn in range(numColumns-1,-1,-1):

				dp[currRow][currColumn] = grid[currRow][currColumn]

				if (currRow,currColumn) != (numRows-1,numColumns-1):

					down = dp[currRow+1][currColumn] if currRow+1<numRows else float('inf')
					right = dp[currRow][currColumn+1] if currColumn+1<numColumns else float('inf')

					dp[currRow][currColumn] += min(down,right)

		return dp[0][0]