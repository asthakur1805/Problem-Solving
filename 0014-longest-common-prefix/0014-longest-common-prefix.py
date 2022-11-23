class Solution:

	def longestCommonPrefix(self, inputStrings):

		inputStrings.sort()

		firstString, lastString = inputStrings[0], inputStrings[-1]

		resultPrefix = []

		for charIndex in range(len(firstString)):

			if firstString[charIndex] != lastString[charIndex]:
				break

			resultPrefix.append(firstString[charIndex])

		return ''.join(resultPrefix)

