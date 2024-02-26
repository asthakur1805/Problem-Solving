class Solution:

	def minFallingPathSum(self,matrix):

		numRows, numColumns = len(matrix), len(matrix[0])

		dp = [[0]*numColumns for _ in range(numRows)]

		for currRow in range(numRows-1,-1,-1):

			for currColumn in range(numColumns-1,-1,-1):

				dp[currRow][currColumn] = matrix[currRow][currColumn]

				if currRow < numRows-1:

					downLeft = dp[currRow+1][currColumn-1] if currColumn >= 1 else float('inf')
					down = dp[currRow+1][currColumn]
					downRight = dp[currRow+1][currColumn+1] if currColumn < numRows-1 else float('inf')

					dp[currRow][currColumn] += min(downLeft,down,downRight)

		result = float('inf')

		for currColumn in range(numColumns):

			result = min(result,dp[0][currColumn])

		return result

				