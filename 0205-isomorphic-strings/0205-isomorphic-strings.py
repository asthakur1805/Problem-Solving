class Solution:

	def isIsomorphic(self, firstStr, secondStr):

		firstMap, secondMap = [0]*255, [0]*255

		for index, (firstChar, secondChar) in enumerate(zip(firstStr, secondStr)):

			if firstMap[ord(firstChar)] != secondMap[ord(secondChar)]:

				return False

			firstMap[ord(firstChar)], secondMap[ord(secondChar)] = index+1, index+1

		return True