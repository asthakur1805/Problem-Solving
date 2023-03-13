class Solution:

	def intersect(self, firstList, secondList):

		result = []

		firstList.sort()

		secondList.sort()

		firstIndex, secondIndex = 0, 0

		while firstIndex < len(firstList) and secondIndex < len(secondList):

			if firstList[firstIndex] == secondList[secondIndex]:

				result.append(firstList[firstIndex])

				firstIndex, secondIndex = firstIndex + 1, secondIndex + 1

			elif firstList[firstIndex] < secondList[secondIndex]:

				firstIndex += 1

			else:

				secondIndex += 1

		return result