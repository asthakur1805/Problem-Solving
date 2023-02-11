class Solution:

	def searchMatrix(self, matrix, target):

		for row in range(len(matrix)):

			for column in range(len(matrix[row])):

				if matrix[row][column] == target:

					return True

		return False