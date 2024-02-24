class Solution:

	def minPathSum(self,grid):

		numRows, numColumns = len(grid), len(grid[0])

		prev = [0]*numColumns

		for currRow in range(numRows-1,-1,-1):

			dp = [0]*numColumns

			for currColumn in range(numColumns-1,-1,-1):

				dp[currColumn] = grid[currRow][currColumn]

				if (currRow,currColumn) != (numRows-1,numColumns-1):

					down = prev[currColumn] if currRow+1<numRows else float('inf')
					right = dp[currColumn+1] if currColumn+1<numColumns else float('inf')

					dp[currColumn] += min(down,right)

			prev = dp

		return prev[0]