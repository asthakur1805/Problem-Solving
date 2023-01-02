class Solution:

	def titleToNumber(self, columnTitle):

		columnNumber = 0

		for columnCharacter in columnTitle:

			digit = ord(columnCharacter) - ord('A') + 1

			columnNumber = columnNumber * 26 + digit

		return columnNumber