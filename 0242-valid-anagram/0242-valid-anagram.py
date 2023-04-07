class Solution:

	def isAnagram(self, firstStr, secondStr):

		if len(firstStr) != len(secondStr):

			return False

		countsFirstStr, countsSecondStr = {}, {}

		for char in firstStr:

			countsFirstStr[char] = countsFirstStr.get(char, 0) + 1

		for char in secondStr:

			countsSecondStr[char] = countsSecondStr.get(char, 0) + 1

		return countsFirstStr == countsSecondStr