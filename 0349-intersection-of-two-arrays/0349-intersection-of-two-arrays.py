class Solution:

	def intersection(self, firstList, secondList):

		result = []

		firstList.sort()

		secondList.sort()

		firstIndex, secondIndex = 0, 0

		while firstIndex < len(firstList) and secondIndex < len(secondList):

			if firstList[firstIndex] < secondList[secondIndex]:

				firstIndex += 1

			elif secondList[secondIndex] < firstList[firstIndex]:

				secondIndex += 1

			else:

				if not result or result[-1] != firstList[firstIndex]:

					result.append(firstList[firstIndex])

				firstIndex += 1

				secondIndex += 1

		return result