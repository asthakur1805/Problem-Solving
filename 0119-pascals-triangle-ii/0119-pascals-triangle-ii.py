class Solution:

	def getRow(self, rowIndex):

		result = [[1]]

		for rowNumber in range(1, rowIndex+1):

			rowResult = [1]

			for columnNumber in range(1, rowNumber):

				rowResult.append(result[rowNumber-1][columnNumber] + result[rowNumber-1][columnNumber-1])

			rowResult.append(1)

			result.append(rowResult)

		return result[rowIndex]
			
