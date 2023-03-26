class Solution:

	def convertToTitle(self, columnNumber):

		result = []

		while columnNumber:

			columnNumber -= 1

			columnValue = columnNumber % 26

			result.append(chr(columnValue + ord('A')))

			columnNumber //= 26

		result.reverse()

		return ''.join(result)