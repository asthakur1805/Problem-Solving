class Solution:

	def searchMatrix(self, matrix, target):

		for row in range(len(matrix)):

			if self.binarySearch(matrix, row, target):

				return True

		return False

	def binarySearch(self, matrix, row, target):

		left, right = 0, len(matrix[row])-1

		while left <= right:

			mid = left + (right - left) // 2

			if matrix[row][mid] == target:
	
				return True

			if matrix[row][mid] < target:

				left = mid + 1

			else:

				right = mid - 1

		return False
