class Solution:

	def uniquePaths(self,numRows,numColumns):

		return self.helper(0,0,numRows,numColumns,{})

	def helper(self,currRow,currColumn,numRows,numColumns,cache):

		if currRow > numRows or currColumn > numColumns:

			return 0

		if (currRow,currColumn) == (numRows-1,numColumns-1):

			return 1

		if (currRow,currColumn) in cache:

			return cache[(currRow,currColumn)]

		down = self.helper(currRow+1,currColumn,numRows,numColumns,cache)
		right = self.helper(currRow,currColumn+1,numRows,numColumns,cache)

		cache[(currRow,currColumn)] = down+right
		return cache[(currRow,currColumn)]
		 