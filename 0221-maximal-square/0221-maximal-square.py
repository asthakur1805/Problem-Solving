class Solution:

	def maximalSquare(self,matrix):

		self.maxSide = 0

		prev = [0]*(len(matrix[0])+1)

		for currRow in range(1,len(matrix)+1):
			
			dp = [0]*(len(matrix[0])+1)

			for currColumn in range(1,len(matrix[0])+1):

				left = dp[currColumn-1]
				top = prev[currColumn]
				diagonal = prev[currColumn-1]

				if matrix[currRow-1][currColumn-1] == '1':

					dp[currColumn] = 1+min(left,top,diagonal)
					self.maxSide = max(self.maxSide,dp[currColumn])

			prev = dp
					
		return self.maxSide ** 2
