class Solution:

	def isAnagram(self, firstStr, secondStr):

		if len(firstStr) != len(secondStr):

			return False

		countsFirstStr, countsSecondStr = [0]*26, [0]*26

		for index in range(len(firstStr)):

			countsFirstStr[ord(firstStr[index])-ord('a')] += 1
			countsSecondStr[ord(secondStr[index])-ord('a')] += 1

		return countsFirstStr == countsSecondStr