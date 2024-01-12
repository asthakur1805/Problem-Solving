class Solution:

	def uniquePaths(self,numRows,numColumns):

		dp = [[0]*numColumns for _ in range(numRows)]

		for currRow in range(numRows-1,-1,-1):

			for currColumn in range(numColumns-1,-1,-1):

				if (currRow,currColumn) == (numRows-1,numColumns-1):

					dp[currRow][currColumn] = 1

				else:

					right = dp[currRow][currColumn+1] if currColumn+1<numColumns else 0

					down = dp[currRow+1][currColumn] if currRow+1<numRows else 0

					dp[currRow][currColumn] = right+down

		return dp[0][0]

			