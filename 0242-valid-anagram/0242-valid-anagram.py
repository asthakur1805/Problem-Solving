class Solution:

	def isAnagram(self, firstStr, secondStr):

		if len(firstStr) != len(secondStr):

			return False

		countFirst, countSecond = {}, {}

		for index in range(len(firstStr)):

			countFirst[firstStr[index]] = countFirst.get(firstStr[index], 0 ) + 1

			countSecond[secondStr[index]] = countSecond.get(secondStr[index], 0) + 1

		for char in countFirst:

			if countFirst[char] != countSecond.get(char, 0):

				return False

		return True
		