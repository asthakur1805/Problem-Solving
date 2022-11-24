class Solution:

	def titleToNumber(self, columnTitle):

		columnNumber = 0

		for columnChar in columnTitle:

			charValue = ord(columnChar) - ord('A') + 1

			columnNumber = columnNumber * 26 + charValue

		return columnNumber