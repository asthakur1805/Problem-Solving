class Solution:

	def longestCommonPrefix(self, inputStrings):

		inputStrings.sort()

		resultPrefix = []

		firstWord, lastWord = inputStrings[0], inputStrings[-1]

		for index in range(len(firstWord)):

			if firstWord[index] != lastWord[index]:

				break

			resultPrefix.append(firstWord[index])

		return ''.join(resultPrefix)