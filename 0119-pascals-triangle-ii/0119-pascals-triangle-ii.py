class Solution:

	def getRow(self, index):

		rowResult = [1]

		for rowIndex in range(1, index+1):

			columnIndex = len(rowResult) - 1

			for _ in range(rowIndex-1):

				rowResult[columnIndex] += rowResult[columnIndex-1]

				columnIndex -= 1

			rowResult.append(1)

		return rowResult