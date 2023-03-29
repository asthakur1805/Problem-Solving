class Solution:

	def isIsomorphic(self, firstStr, secondStr):

		if len(firstStr) != len(secondStr):

			return False

		firstMap, secondMap = [0] * 256, [0] * 256

		for index, (firstChar, secondChar) in enumerate(zip(firstStr, secondStr)):

			if firstMap[ord(firstChar)] != secondMap[ord(secondChar)]:

				return False

			firstMap[ord(firstChar)], secondMap[ord(secondChar)] = index + 1, index + 1

		return True
			