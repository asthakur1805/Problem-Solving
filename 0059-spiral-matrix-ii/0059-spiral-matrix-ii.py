class Solution:

	def generateMatrix(self, base):

		matrix = [[0 for _ in range(base)] for _ in range(base)]

		left, right, top, bottom = 0, base, 0, base

		count = 1

		while left < right and top < bottom:

			for column in range(left, right):

				matrix[top][column] = count

				count += 1

			top += 1

			for row in range(top, bottom):

				matrix[row][right-1] = count

				count += 1

			right -= 1

			for column in range(right-1, left-1, -1):

				matrix[bottom-1][column] = count

				count += 1

			bottom -= 1

			for row in range(bottom-1, top-1, -1):

				matrix[row][left] = count

				count += 1

			left += 1

		return matrix