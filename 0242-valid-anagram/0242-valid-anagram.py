class Solution:

	def isAnagram(self, firstStr, secondStr):

		countsFirstStr, countsSecondStr = [0]*26,[0]*26

		for char in firstStr:

			countsFirstStr[ord(char)-ord('a')] += 1

		for char in secondStr:

			countsSecondStr[ord(char)-ord('a')] += 1

		return countsFirstStr == countsSecondStr

			