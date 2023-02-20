class Solution:

	def firstUniqChar(self, inputStr):

		charCounts = {}

		for char in inputStr:

			charCounts[char] = charCounts.get(char, 0) + 1

		for index, char in enumerate(inputStr):

			if charCounts[char] == 1:

				return index

		return -1