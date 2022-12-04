class Solution:

	def getRow(self, rowIndex):

		rowResult = [1]

		for rowNumber in range(1, rowIndex+1):

			columnIndex = len(rowResult)-1

			for _ in range(rowNumber-1):

				rowResult[columnIndex] += rowResult[columnIndex-1]

				columnIndex -= 1

			rowResult.append(1)

		return rowResult