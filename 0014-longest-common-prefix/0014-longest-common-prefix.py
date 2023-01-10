class Solution:

	def longestCommonPrefix(self, inputStrings):

		resultPrefix = []

		for index, character in enumerate(inputStrings[0]):

			for remainingIndex in range(1,len(inputStrings)):

				word = inputStrings[remainingIndex]

				if index == len(word) or word[index] != character:

					return ''.join(resultPrefix)

			resultPrefix.append(character)

		return ''.join(resultPrefix)