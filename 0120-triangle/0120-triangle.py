class Solution:

	def minimumTotal(self,triangle):

		numRows = len(triangle) 

		return self.helper(triangle,0,0,numRows,{})

	def helper(self,triangle,currRow,currColumn,numRows,cache):

		if currRow == numRows-1:

			return triangle[currRow][currColumn]

		if (currRow,currColumn) in cache:

			return cache[(currRow,currColumn)]

		down = self.helper(triangle,currRow+1,currColumn,numRows,cache)
		diagonal = self.helper(triangle,currRow+1,currColumn+1,numRows,cache)

		cache[(currRow,currColumn)] = triangle[currRow][currColumn] + min(down,diagonal)

		return cache[(currRow,currColumn)]