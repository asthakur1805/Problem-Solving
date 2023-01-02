class Solution:

	def convertToTitle(self, columnNumber):

		columnTitle = []

		while columnNumber:

			digit = (columnNumber - 1) % 26

			columnCharacter = chr(digit + ord('A'))

			columnTitle.append(columnCharacter)

			columnNumber = (columnNumber - 1) // 26

		columnTitle.reverse()

		return ''.join(columnTitle)