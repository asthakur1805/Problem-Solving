class Solution:

	def cherryPickup(self,grid):

		numRows, numColumns = len(grid), len(grid[0])

		dp = [[[0]*numColumns for _ in range(numColumns)] for _ in range(numRows)]

		for row in range(numRows-1,-1,-1):

			for firstColumn in range(numColumns-1,-1,-1):

				for secondColumn in range(numColumns-1,-1,-1):

					if firstColumn == secondColumn:

						dp[row][firstColumn][secondColumn] = grid[row][firstColumn]

					else:

						dp[row][firstColumn][secondColumn] = grid[row][firstColumn]+grid[row][secondColumn]

					if row < numRows-1:

						maxResult = 0

						for firstColumnDirection in range(-1,2):

							for secondColumnDirection in range(-1,2):

								maxResult = max(maxResult,dp[row+1][firstColumn+firstColumnDirection][secondColumn+secondColumnDirection] if (0 <= firstColumn+firstColumnDirection < numColumns and 0 <= secondColumn+secondColumnDirection < numColumns) else 0)

						dp[row][firstColumn][secondColumn] += maxResult


		return dp[0][0][numColumns-1]