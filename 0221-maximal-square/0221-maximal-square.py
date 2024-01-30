class Solution:

	def maximalSquare(self,matrix):

		self.maxSide = 0

		dp = [[0]*(len(matrix[0])+1) for _ in range(len(matrix)+1)]

		for currRow in range(1,len(matrix)+1):

			for currColumn in range(1,len(matrix[0])+1):

				left = dp[currRow][currColumn-1]
				top = dp[currRow-1][currColumn]
				diagonal = dp[currRow-1][currColumn-1]

				if matrix[currRow-1][currColumn-1] == '1':

					dp[currRow][currColumn] = 1+min(left,top,diagonal)
					self.maxSide = max(self.maxSide,dp[currRow][currColumn])
					
		return self.maxSide ** 2