class Solution:

	def searchMatrix(self, matrix, target):

		rowPointer, columnPointer = len(matrix)-1, 0

		while rowPointer >= 0 and columnPointer <= len(matrix[0])-1:

			if matrix[rowPointer][columnPointer] == target:

				return True

			if matrix[rowPointer][columnPointer] > target:

				rowPointer -= 1

			else:

				columnPointer += 1

		return False

		