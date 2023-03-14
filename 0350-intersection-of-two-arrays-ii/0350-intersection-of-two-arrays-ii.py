class Solution:

	def intersect(self, firstList, secondList):

		if len(secondList) < len(firstList):

			return self.intersect(secondList, firstList)

		result = []

		counts = {}

		for char in firstList:

			counts[char] = counts.get(char,0) + 1

		for char in secondList:

			if counts.get(char,0) > 0:

				result.append(char)

				counts[char] -= 1

		return result

				