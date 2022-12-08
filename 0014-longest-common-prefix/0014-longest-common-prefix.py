class Solution:
	
	def longestCommonPrefix(self, inputStrs):

		resultPrefix = []

		for index, character in enumerate(inputStrs[0]):

			for remaining in range(1, len(inputStrs)):

				word = inputStrs[remaining]

				if index == len(word) or word[index] != character:

					return ''.join(resultPrefix)


			resultPrefix.append(character)

		return ''.join(resultPrefix)