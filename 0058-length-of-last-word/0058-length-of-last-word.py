class Solution:

	def lengthOfLastWord(self, inputStr):

		charIndex = len(inputStr)-1

		while inputStr[charIndex] == ' ':

			charIndex -= 1

		resultLength = 0

		while charIndex >= 0 and inputStr[charIndex] != ' ':

			resultLength += 1
			charIndex -= 1

		return resultLength