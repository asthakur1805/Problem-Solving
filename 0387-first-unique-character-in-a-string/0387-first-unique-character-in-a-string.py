class Solution:

	def firstUniqChar(self, inputStr):

		counts = {}

		for char in inputStr:

			counts[char] = counts.get(char, 0) + 1

		for index, char in enumerate(inputStr):

			if counts[char] == 1:

				return index

		return -1