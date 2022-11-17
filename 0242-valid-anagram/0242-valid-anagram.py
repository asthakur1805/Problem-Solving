class Solution:

	def isAnagram(self, firstStr, secondStr):

		if len(firstStr) != len(secondStr):

			return False

		firstStrMap, secondStrMap = self.getCounts(firstStr), self.getCounts(secondStr)

		for currKey in firstStrMap.keys():

			if currKey not in secondStrMap or firstStrMap[currKey] != secondStrMap[currKey]:

				return False

		return True

	def getCounts(self, inputStr):

		outputMap = {}

		for character in inputStr:

			outputMap[character] = outputMap.get(character, 0) + 1

		return outputMap

	