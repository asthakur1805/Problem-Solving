class Solution:

	def generate(self, numRows):

		if numRows < 1:

			return

		result = [[1]]

		for rowIndex in range(1, numRows):

			rowResult = [1]

			for columnIndex in range(1, rowIndex):

				rowResult.append(result[rowIndex-1][columnIndex] + result[rowIndex-1][columnIndex-1])

			rowResult.append(1)

			result.append(rowResult)

		return result