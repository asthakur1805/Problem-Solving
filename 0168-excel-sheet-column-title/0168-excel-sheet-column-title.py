class Solution:

	def convertToTitle(self, columnNumber):

		columnTitle = []

		while columnNumber:

			charValue = (columnNumber - 1) % 26

			columnTitle.append(chr(charValue + ord('A')))

			columnNumber = (columnNumber - 1) // 26

		columnTitle.reverse()

		return ''.join(columnTitle)