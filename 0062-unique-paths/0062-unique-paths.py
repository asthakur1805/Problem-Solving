class Solution:

	def uniquePaths(self,numRows,numColumns):

		prev = [0]*numColumns

		for currRow in range(numRows-1,-1,-1):

			dp = [0]*numColumns

			for currColumn in range(numColumns-1,-1,-1):

				if (currRow,currColumn) == (numRows-1,numColumns-1):

					dp[currColumn] = 1

				else:

					down = prev[currColumn] if currRow+1<numRows else 0
					right = dp[currColumn+1] if currColumn+1<numColumns else 0

					dp[currColumn] = down+right

			prev = dp

		return prev[0]

		