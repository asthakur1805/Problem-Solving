class Solution:

	def generate(self, numRows):

		resultTriangle = [[1]]

		for rowIndex in range(1,numRows):

			rowResult = [1]

			for columnIndex in range(1, rowIndex):

				rowResult.append(resultTriangle[rowIndex-1][columnIndex] + resultTriangle[rowIndex-1][columnIndex-1])

			rowResult.append(1)

			resultTriangle.append(rowResult)

		return resultTriangle