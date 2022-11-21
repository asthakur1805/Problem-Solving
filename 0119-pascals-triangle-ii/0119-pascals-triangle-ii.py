class Solution:

	def getRow(self, index):

		triangleResult = [[1]]

		for rowIndex in range(1, index+1):

			rowResult = [1]

			for columnIndex in range(1, rowIndex):

				rowResult.append(triangleResult[rowIndex-1][columnIndex] + triangleResult[rowIndex-1][columnIndex-1])

			rowResult.append(1)

			triangleResult.append(rowResult)

		return triangleResult[-1]


