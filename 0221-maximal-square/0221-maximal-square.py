class Solution:

	def maximalSquare(self,matrix):

		self.maxSide = 0

		self.helper(matrix,len(matrix)-1,len(matrix[0])-1,{})

		return self.maxSide ** 2

	def helper(self,matrix,currRow,currColumn,cache):

		if currRow < 0 or currColumn < 0: 

			return 0

		if (currRow,currColumn) in cache:

			return cache[(currRow,currColumn)]

		left = self.helper(matrix,currRow,currColumn-1,cache)
		top = self.helper(matrix,currRow-1,currColumn,cache)
		diagonal = self.helper(matrix,currRow-1,currColumn-1,cache)

		if matrix[currRow][currColumn] == '1':

			cache[(currRow,currColumn)] = 1+min(left,top,diagonal)
			self.maxSide = max(self.maxSide,cache[(currRow,currColumn)])
			return cache[(currRow,currColumn)]

		cache[(currRow,currColumn)] = 0
		return 0