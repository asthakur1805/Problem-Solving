class Solution:

	def generateMatrix(self, rankMatrix):

		matrix = [[0 for _ in range(rankMatrix)] for _ in range(rankMatrix)]

		matrixValue = 1

		left, right, top, bottom = 0, len(matrix), 0, len(matrix)

		while left < right and top < bottom:

			for column in range(left, right):

				matrix[top][column] = matrixValue

				matrixValue += 1

			top += 1

			for row in range(top, bottom):

				matrix[row][right-1] = matrixValue

				matrixValue += 1

			right -= 1

			for column in range(right-1, left-1, -1):

				matrix[bottom-1][column] = matrixValue

				matrixValue += 1

			bottom -= 1

			for row in range(bottom-1, top-1, -1):

				matrix[row][left] = matrixValue

				matrixValue += 1

			left += 1

		return matrix