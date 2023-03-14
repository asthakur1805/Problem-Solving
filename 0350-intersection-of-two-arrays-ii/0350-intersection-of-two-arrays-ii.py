class Solution:

	def intersect(self, firstList, secondList):

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

				result.append(firstList[firstIndex])

				firstIndex += 1

				secondIndex += 1

		return result