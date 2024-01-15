class Solution:

	def cherryPickup(self,grid):

		numRows, numColumns = len(grid), len(grid[0])

		prev = [[0]*numColumns for _ in range(numColumns)]

		for row in range(numRows-1,-1,-1):

			dp = [[0]*numColumns for _ in range(numColumns)]

			for firstColumn in range(numColumns-1,-1,-1):

				for secondColumn in range(numColumns-1,-1,-1):

					if firstColumn == secondColumn:

						dp[firstColumn][secondColumn] = grid[row][firstColumn]

					else:

						dp[firstColumn][secondColumn] = grid[row][firstColumn]+grid[row][secondColumn]

					if row < numRows-1:

						maxResult = 0

						for firstColumnDirection in range(-1,2):

							for secondColumnDirection in range(-1,2):

								maxResult = max(maxResult,prev[firstColumn+firstColumnDirection][secondColumn+secondColumnDirection] if (0 <= firstColumn+firstColumnDirection < numColumns and 0 <= secondColumn+secondColumnDirection < numColumns) else 0)

						dp[firstColumn][secondColumn] += maxResult

			prev = dp

		return prev[0][numColumns-1]