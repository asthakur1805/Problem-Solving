class Solution:

	def minFallingPathSum(self,matrix):

		numRows, numColumns = len(matrix), len(matrix[0])

		prev = [0]*numColumns

		for currRow in range(numRows-1,-1,-1):

			dp = [0]*numColumns

			for currColumn in range(numColumns-1,-1,-1):

				dp[currColumn] = matrix[currRow][currColumn]

				if currRow < numRows-1:

					downLeft = prev[currColumn-1] if currColumn >= 1 else float('inf')
					down = prev[currColumn]
					downRight = prev[currColumn+1] if currColumn < numRows-1 else float('inf')

					dp[currColumn] += min(downLeft,down,downRight)

			prev = dp

		result = float('inf')

		for currColumn in range(numColumns):

			result = min(result,prev[currColumn])

		return result

				