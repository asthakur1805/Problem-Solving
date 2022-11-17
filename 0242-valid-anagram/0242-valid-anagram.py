class Solution:

	def isAnagram(self, firstStr, secondStr):

		if len(firstStr) != len(secondStr):
			return False

		firstStrMap, secondStrMap = {}, {}

		for charIndex in range(len(firstStr)):

			firstStrMap[firstStr[charIndex]] = 1 + firstStrMap.get(firstStr[charIndex], 0)

			secondStrMap[secondStr[charIndex]] = 1 + secondStrMap.get(secondStr[charIndex], 0)

		for character in firstStrMap:

			if firstStrMap[character] != secondStrMap.get(character, 0):

				return False

		return True