class Solution:

	def isIsomorphic(self, firstStr, secondStr):

		if len(firstStr) != len(secondStr):

			return False

		firstMap, secondMap = [0] * 256, [0] * 256

		for index in range(len(firstStr)):

			if firstMap[ord(firstStr[index])] != secondMap[ord(secondStr[index])]:

				return False

			firstMap[ord(firstStr[index])] = index + 1
			secondMap[ord(secondStr[index])] = index + 1

		return True