class Solution:

	def lengthOfLastWord(self, inputStr):

		index = len(inputStr)-1

		while inputStr[index] == ' ':

			index -= 1

		resultLength = 0

		while index >= 0 and inputStr[index] != ' ':

			resultLength += 1
			index -= 1

		return resultLength
