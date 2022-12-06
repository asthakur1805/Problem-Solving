class Solution:

	def getRow(self, index):

		result = [[1]]

		for rowIndex in range(1, index+1):

			rowResult = [1]

			for columnIndex in range(1, rowIndex):

				rowResult.append(result[rowIndex-1][columnIndex] + result[rowIndex-1][columnIndex-1])

			rowResult.append(1)

			result.append(rowResult)

		return result[index]

