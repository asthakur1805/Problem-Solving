class Solution:

	def spiralOrder(self, matrix):

		left, right, top, bottom = 0, len(matrix[0]), 0, len(matrix)

		result = []

		while left < right and top < bottom:

			for column in range(left, right):

				result.append(matrix[top][column])

			top += 1

			for row in range(top, bottom):

				result.append(matrix[row][right-1])

			right -= 1

			if not(left < right and top < bottom):

				break

			for column in range(right-1, left-1, -1):

				result.append(matrix[bottom-1][column])

			bottom -= 1

			for row in range(bottom-1, top-1, -1):

				result.append(matrix[row][left])

			left += 1

		return result