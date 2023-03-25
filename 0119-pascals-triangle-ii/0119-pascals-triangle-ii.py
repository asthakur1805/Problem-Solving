class Solution:

	def getRow(self, index):

		rowResult = [1]

		for row in range(1, index+1):

			column = len(rowResult)-1

			for _ in range(row-1):

				rowResult[column] += rowResult[column-1]

				column -= 1

			rowResult.append(1)

		return rowResult