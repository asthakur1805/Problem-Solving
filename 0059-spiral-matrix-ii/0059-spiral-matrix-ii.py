class Solution:

	def generateMatrix(self, base):

		matrix = [[0] * base for _ in range(base)]

		count = 1

		top, bottom, left, right = 0, base, 0, base

		while top < bottom and left < right:

			for col in range(left, right):

				matrix[top][col] = count
				count += 1

			top += 1

			for row in range(top, bottom):

				matrix[row][right-1] = count
				count += 1

			right -= 1

			for col in range(right-1, left-1, -1):

				matrix[bottom-1][col] = count
				count += 1

			bottom -= 1

			for row in range(bottom-1, top-1, -1):

				matrix[row][left] = count
				count += 1

			left += 1

		return matrix
			