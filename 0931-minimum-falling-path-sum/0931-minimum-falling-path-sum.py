class Solution:

	def minFallingPathSum(self,matrix):

		numRows, numColumns = len(matrix), len(matrix[0])

		result = float('inf')

		for currColumn in range(numColumns):

			result = min(result,self.helper(matrix,0,currColumn,numRows,numColumns,{}))

		return result

	def helper(self,matrix,currRow,currColumn,numRows,numColumns,cache):

		if currColumn < 0 or currColumn >= numColumns:

			return float('inf')

		if (currRow,currColumn) in cache:

			return cache[(currRow,currColumn)]

		result = matrix[currRow][currColumn]

		if currRow < numRows-1:

			downLeft = self.helper(matrix,currRow+1,currColumn-1,numRows,numColumns,cache)
			down = self.helper(matrix,currRow+1,currColumn,numRows,numColumns,cache)
			downRight = self.helper(matrix,currRow+1,currColumn+1,numRows,numColumns,cache)

			result += min(downLeft,down,downRight)

		cache[(currRow,currColumn)] = result
		return result