class Solution:

	def generate(self, numRows):

		if numRows == 0:

			return

		triangleResult = [[1]]

		for rowIndex in range(1, numRows):

			rowResult = [1]

			for columnIndex in range(1, rowIndex):

				rowResult.append(triangleResult[rowIndex-1][columnIndex] + triangleResult[rowIndex-1][columnIndex-1])

			rowResult.append(1)

			triangleResult.append(rowResult)

		return triangleResult