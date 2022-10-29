class Solution:

	def convert(self,inputStr, rowCount):

		if rowCount == 1:

			return inputStr

		inputLength, stepSize = len(inputStr), 2 * (rowCount - 1)

		resultStr = []

		for rowNumber in range(rowCount):

			for vertical in range(rowNumber, inputLength, stepSize):

				resultStr.append(inputStr[vertical])

				if rowNumber != 0 and rowNumber != rowCount - 1:

					slant = vertical + stepSize - 2 * rowNumber

					if slant < inputLength:

						resultStr.append(inputStr[slant])

		return ''.join(resultStr)