class Solution:

	def titleToNumber(self, columnTitle):

		columnNumber = 0

		for columnCharacter in columnTitle:

			faceValue = ord(columnCharacter) - ord('A') + 1

			columnNumber = columnNumber * 26 + faceValue

		return columnNumber