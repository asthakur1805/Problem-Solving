class Solution:

	def longestCommonPrefix(self, inputStrings):

		resultPrefix = []

		for charIndex, character in enumerate(inputStrings[0]):

			for remaining in range(1, len(inputStrings)):

				word = inputStrings[remaining]

				if charIndex == len(word) or word[charIndex] != character:

					return ''.join(resultPrefix)

			resultPrefix.append(character)

		return ''.join(resultPrefix)