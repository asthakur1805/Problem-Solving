class Solution:

	def longestCommonPrefix(self, inputStrings):

		result = []

		for index, character in enumerate(inputStrings[0]):

			for remaining in range(1, len(inputStrings)):

				word = inputStrings[remaining]

				if index == len(word) or word[index] != character:

					return ''.join(result)

			result.append(character)

		return ''.join(result)