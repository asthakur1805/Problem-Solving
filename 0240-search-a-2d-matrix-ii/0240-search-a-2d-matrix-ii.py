class Solution:

	def searchMatrix(self, matrix, target):

		for row in range(len(matrix)):

			for column in range(len(matrix[0])):

				if matrix[row][column] == target:

					return True

		return False