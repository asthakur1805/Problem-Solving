class Solution:

	def longestCommonPrefix(self, inputStrings):

		inputStrings.sort()

		firstWord, lastWord = inputStrings[0], inputStrings[-1]

		result = []

		for index in range(len(firstWord)):

			if firstWord[index] != lastWord[index]:

				break

			result.append(firstWord[index])

		return ''.join(result)