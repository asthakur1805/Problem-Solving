class Solution:

	def convertToTitle(self, columnNumber):

		columnTitle = []

		while columnNumber:

			faceValue = (columnNumber - 1) % 26

			columnCharacter = chr(faceValue + ord('A'))

			columnTitle.append(columnCharacter)

			columnNumber = (columnNumber - 1) // 26

		columnTitle.reverse()

		return ''.join(columnTitle)