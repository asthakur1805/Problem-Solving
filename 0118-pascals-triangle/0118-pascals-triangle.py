class Solution:

	def generate(self, numRows):

		result = [[1]]

		for row in range(1, numRows):

			rowResult = [1]

			for column in range(1, row):

				rowResult.append(result[row-1][column] + result[row-1][column-1])

			rowResult.append(1)

			result.append(rowResult)

		return result