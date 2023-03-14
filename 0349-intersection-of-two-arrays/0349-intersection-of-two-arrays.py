class Solution:

	def intersection(self, firstList, secondList):

		if len(firstList) < len(secondList):

			return self.intersection(secondList, firstList)

		result = []

		numSet = set()

		for num in firstList:

			numSet.add(num)

		for num in secondList:

			if num in numSet:

				result.append(num)

				numSet.remove(num)

		return result

