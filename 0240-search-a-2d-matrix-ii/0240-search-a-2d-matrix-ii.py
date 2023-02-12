class Solution:

	def searchMatrix(self, matrix, target):

		row, column = len(matrix)-1, 0

		while row >= 0 and column <= len(matrix[0])-1:

			cellValue = matrix[row][column]

			if  cellValue == target:

				return True

			elif cellValue < target:

				column += 1

			else:

				row -= 1

		return False