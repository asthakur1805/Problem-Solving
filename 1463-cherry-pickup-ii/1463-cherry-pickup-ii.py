class Solution:

	def cherryPickup(self,grid):

		numRows, numColumns = len(grid), len(grid[0])

		dp = [[[0]*numColumns for _ in range(numColumns)] for _ in range(numRows)] 

		for currRow in range(numRows-1,-1,-1):

			for firstColumn in range(numColumns-1,-1,-1):

				for secondColumn in range(numColumns-1,-1,-1):

					dp[currRow][firstColumn][secondColumn] = grid[currRow][firstColumn]

					if firstColumn != secondColumn:

						dp[currRow][firstColumn][secondColumn] += grid[currRow][secondColumn]

					if currRow < numRows-1:

						currMax = 0

						for firstColumnDirection in range(-1,2):

							for secondColumnDirection in range(-1,2):

								firstNextColumn, secondNextColumn = firstColumn+firstColumnDirection, secondColumn+secondColumnDirection

								if firstNextColumn >= 0 and firstNextColumn < numColumns and secondNextColumn >= 0 and secondNextColumn < numColumns:

									currMax = max(currMax,dp[currRow+1][firstNextColumn][secondNextColumn])

						dp[currRow][firstColumn][secondColumn] += currMax

		return dp[0][0][numColumns-1]
