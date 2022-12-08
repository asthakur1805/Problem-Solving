class Solution:

	def longestCommonPrefix(self, inputStrs):

		inputStrs.sort()

		firstWord, lastWord = inputStrs[0], inputStrs[-1]

		resultPrefix = []

		for index in range(len(firstWord)):

			if firstWord[index] != lastWord[index]:

				break

			resultPrefix.append(firstWord[index])

		return ''.join(resultPrefix)