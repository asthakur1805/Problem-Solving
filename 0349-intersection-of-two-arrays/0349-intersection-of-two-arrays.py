class Solution:

	def intersection(self, firstArr, secondArr):

		firstArr.sort()
		secondArr.sort()

		firstIndex, secondIndex, intersectSet = 0, 0, set()

		while firstIndex < len(firstArr) and secondIndex < len(secondArr):

			if firstArr[firstIndex] < secondArr[secondIndex]:

				firstIndex += 1

			elif secondArr[secondIndex] < firstArr[firstIndex]:

				secondIndex += 1

			else:

				intersectSet.add(firstArr[firstIndex])
				firstIndex += 1
				secondIndex += 1

		return list(intersectSet)

		
	