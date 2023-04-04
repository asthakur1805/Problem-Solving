class Solution:

	def searchMatrix(self, matrix, target):

		numRows, numColumns = len(matrix), len(matrix[0])

		for row in range(numRows):

			for col in range(numColumns):

				if matrix[row][col] == target:

					return True

		return False