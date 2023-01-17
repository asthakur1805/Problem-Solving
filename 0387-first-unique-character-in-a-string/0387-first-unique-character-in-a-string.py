class Solution:

	def firstUniqChar(self, inputStr):

		counts = {}

		for inputChar in inputStr:

			counts[inputChar] = counts.get(inputChar, 0) + 1

		for index, inputChar in enumerate(inputStr):

			if counts[inputChar] == 1:

				return index

		return -1