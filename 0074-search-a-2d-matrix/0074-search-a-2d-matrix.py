class Solution:

	def searchMatrix(self, matrix, target):

		numRows, numColumns = len(matrix), len(matrix[0])

		for rowIndex in range(numRows):

			for columnIndex in range(numColumns):

				if matrix[rowIndex][columnIndex] == target:

					return True

		return False
