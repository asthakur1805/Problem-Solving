class Solution:

	def getRow(self, index):

		triangle = [[1]]

		for rowIndex in range(1,index + 1):

			rowResult = [1]

			for columnIndex in range(1, rowIndex):

				rowResult.append(triangle[rowIndex-1][columnIndex] + triangle[rowIndex-1][columnIndex-1])

			rowResult.append(1)

			triangle.append(rowResult)

		return triangle[index]

			