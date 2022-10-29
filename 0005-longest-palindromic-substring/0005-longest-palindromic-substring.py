class Solution:

	def longestPalindrome(self, inputStr):

		resultLength, inputLength = 0, len(inputStr)

		for index in range(inputLength):

			# Odd palindromes
	
			leftIndex, rightIndex = index, index

			while leftIndex >= 0 and rightIndex < inputLength and inputStr[leftIndex] == inputStr[rightIndex]:

				if rightIndex - leftIndex + 1 > resultLength:

					resultStartIndex, resultEndIndex, resultLength = leftIndex, rightIndex, rightIndex - leftIndex + 1

				leftIndex -= 1

				rightIndex += 1

			leftIndex, rightIndex = index, index + 1

			while leftIndex >= 0 and rightIndex < inputLength and inputStr[leftIndex] == inputStr[rightIndex]:

				if rightIndex - leftIndex + 1 > resultLength:

					resultStartIndex, resultEndIndex, resultLength = leftIndex, rightIndex, rightIndex - leftIndex + 1

				leftIndex -= 1

				rightIndex += 1

		return inputStr[resultStartIndex: resultEndIndex + 1]